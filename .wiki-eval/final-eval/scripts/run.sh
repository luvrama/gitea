#!/bin/bash
# run.sh — Final evaluation runner
# Usage: ./run.sh <query_number> [approach]
#   ./run.sh 1 baseline    — Run baseline only for Q1
#   ./run.sh 1 3stage      — Run 3-stage only for Q1
#   ./run.sh 1             — Run both approaches for Q1
#   ./run.sh all           — Run everything

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
EVAL_DIR="$(dirname "$SCRIPT_DIR")"
PROJECT_DIR="$(dirname "$(dirname "$EVAL_DIR")")"
WIKI_DIR="$PROJECT_DIR/.project-analysis/wiki"
GRAPH_WIKI_DIR="$PROJECT_DIR/.project-analysis/graphify-out/wiki"
WIKI_INDEX="$(dirname "$EVAL_DIR")/wiki-index.json"
GRAPH_INDEX="$(dirname "$EVAL_DIR")/wiki-index-graph.json"

QUERIES_DIR="$EVAL_DIR/queries"
RESULTS_DIR="$EVAL_DIR/results"

clean_ansi() {
    python3 -c "
import re, sys
content = sys.stdin.read()
clean = re.sub(r'\x1B\[[0-9;]*[a-zA-Z]', '', content)
clean = re.sub(r'\x1B\[\?[0-9]*[a-zA-Z]', '', clean)
sys.stdout.write(clean)
"
}

run_baseline() {
    local q=$1
    local out="$RESULTS_DIR/baseline/q${q}"
    mkdir -p "$out"
    
    echo "  [baseline] Running..."
    python3 -c "
import sys
prompt = open('$SCRIPT_DIR/prompt-baseline.md').read()
query = open('$QUERIES_DIR/q${q}/prompt.txt').read().strip()
sys.stdout.write(prompt.replace('{{QUERY}}', query))
" > "$out/prompt.md"
    
    cd "$PROJECT_DIR"
    kiro-cli chat --no-interactive --trust-all-tools < "$out/prompt.md" > "$out/full-log.txt" 2>&1 || true
    cd "$SCRIPT_DIR"
    
    # Extract credits
    local credits=$(cat "$out/full-log.txt" | clean_ansi | grep -o 'Credits: [0-9.]*' | tail -1 | grep -o '[0-9.]*')
    echo "  [baseline] Done: ${credits:-?} credits"
}

run_3stage() {
    local q=$1
    local out="$RESULTS_DIR/3stage/q${q}"
    mkdir -p "$out"
    
    # Stage 0: Classify
    echo "  [3stage] Classifying..."
    python3 -c "
import sys
prompt = open('$SCRIPT_DIR/prompt-classifier.md').read()
query = open('$QUERIES_DIR/q${q}/prompt.txt').read().strip()
sys.stdout.write(prompt.replace('{{QUERY}}', query))
" > "$out/stage0-prompt.md"
    
    kiro-cli chat --no-interactive --trust-tools= < "$out/stage0-prompt.md" > "$out/stage0-log.txt" 2>&1 || true
    
    local source=$(cat "$out/stage0-log.txt" | clean_ansi | python3 -c "
import sys
content = sys.stdin.read().lower().split('credits')[0]
print('graph' if 'graph' in content else 'wiki')
")
    echo "  [3stage] Source: $source"
    echo "$source" > "$out/classification.txt"
    
    if [ "$source" = "wiki" ]; then
        # Wiki path: select pages → inject → answer
        echo "  [3stage] Wiki path: selecting pages..."
        python3 -c "
import sys
selector = open('$SCRIPT_DIR/prompt-page-selector.md').read()
index = open('$WIKI_INDEX').read()
query = open('$QUERIES_DIR/q${q}/prompt.txt').read().strip()
sys.stdout.write(selector.replace('{{WIKI_INDEX}}', index).replace('{{QUERY}}', query))
" > "$out/stage1-prompt.md"
        
        kiro-cli chat --no-interactive --trust-tools= < "$out/stage1-prompt.md" > "$out/stage1-log.txt" 2>&1 || true
        
        # Extract pages
        cat "$out/stage1-log.txt" | clean_ansi | python3 -c "
import re, json, sys
content = sys.stdin.read()
credits_pos = content.rfind('Credits:')
gt_positions = [m.start() for m in re.finditer(r'^> ', content, re.MULTILINE)]
last_gt = max([p for p in gt_positions if p < credits_pos], default=-1) if credits_pos > 0 else -1
if last_gt >= 0:
    response = content[last_gt:credits_pos]
    start = response.find('[')
    end = response.rfind(']')
    if start >= 0 and end > start:
        try:
            pages = json.loads(response[start:end+1])
            print(json.dumps(pages))
        except: print('[]')
    else: print('[]')
else: print('[]')
" > "$out/selected-pages.json"
        
        local page_count=$(python3 -c "import json; print(len(json.load(open('$out/selected-pages.json'))))")
        echo "  [3stage] Selected $page_count pages"
        
        # Stage 2: Answer from pages
        python3 << EOF
import json, os, re, sys
pages = json.load(open('$out/selected-pages.json'))
wiki_dir = '$WIKI_DIR'
graph_wiki_dir = '$GRAPH_WIKI_DIR'
answerer = open('$SCRIPT_DIR/prompt-answerer.md').read()
query = open('$QUERIES_DIR/q${q}/prompt.txt').read().strip()
wiki_content = ''
for p in pages:
    # Handle both formats: string or object
    path = p['path'] if isinstance(p, dict) else p
    if path.startswith('graph/'):
        full = os.path.join(graph_wiki_dir, path[6:])
    else:
        full = os.path.join(wiki_dir, path)
    if not os.path.exists(full): continue
    wiki_content += f'\n--- FILE: {path} ---\n{open(full).read()}\n'
prompt = answerer.replace('{{WIKI_PAGES}}', wiki_content).replace('{{QUERY}}', query)
with open('$out/stage2-prompt.md', 'w') as f: f.write(prompt)
EOF
        kiro-cli chat --no-interactive --trust-tools= < "$out/stage2-prompt.md" > "$out/stage2-log.txt" 2>&1 || true
        
    else
        # Graph path: LLM + graph_query tool
        echo "  [3stage] Graph path: using graph tool..."
        python3 -c "
import sys
prompt = open('$SCRIPT_DIR/prompt-graph-tool.md').read()
query = open('$QUERIES_DIR/q${q}/prompt.txt').read().strip()
sys.stdout.write(prompt.replace('{{QUERY}}', query))
" > "$out/stage1-prompt.md"
        
        cd "$SCRIPT_DIR"
        kiro-cli chat --no-interactive --trust-all-tools < "$out/stage1-prompt.md" > "$out/stage2-log.txt" 2>&1 || true
    fi
    
    # Extract total credits
    local total=$(python3 -c "
import re, os
total = 0
for f in ['$out/stage0-log.txt', '$out/stage1-log.txt', '$out/stage2-log.txt']:
    if os.path.exists(f):
        content = open(f).read()
        content = re.sub(r'\x1B\[[0-9;]*[a-zA-Z]', '', content)
        m = re.search(r'Credits: ([0-9.]+)', content)
        if m: total += float(m.group(1))
print(f'{total:.2f}')
")
    echo "  [3stage] Done: $total credits"
}

# --- Main ---
QNUM="${1:-all}"
APPROACH="${2:-both}"

if [ "$QNUM" = "all" ]; then
    QUERIES=$(ls "$QUERIES_DIR" | grep -o '[0-9]*' | sort -n)
else
    QUERIES="$QNUM"
fi

for q in $QUERIES; do
    echo "=== Q${q}: $(head -c 70 "$QUERIES_DIR/q${q}/prompt.txt") ==="
    if [ "$APPROACH" = "both" ] || [ "$APPROACH" = "baseline" ]; then
        run_baseline "$q"
    fi
    if [ "$APPROACH" = "both" ] || [ "$APPROACH" = "3stage" ]; then
        run_3stage "$q"
    fi
    echo ""
done
