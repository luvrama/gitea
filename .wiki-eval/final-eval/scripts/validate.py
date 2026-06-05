#!/usr/bin/env python3
"""
validate.py — Full validation (requires kiro-cli for narrative fact-checking)
Computes P/R/F1 for all query types:
- Countable: endpoint ID matching
- Narrative: LLM-based fact-checking (YES/NO per fact)
- Bug localization: file path matching

Usage: python3 validate.py
"""
import json, re, os, sys, subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EVAL_DIR = os.path.dirname(SCRIPT_DIR)
RESULTS_DIR = os.path.join(EVAL_DIR, 'results')
QUERIES_DIR = os.path.join(EVAL_DIR, 'queries')
WIKI_DIR = os.path.join(os.path.dirname(os.path.dirname(EVAL_DIR)), '.project-analysis', 'wiki')
FACTS_FILE = os.path.join(SCRIPT_DIR, 'facts-checklist.json')

def clean_ansi(c):
    c = re.sub(r'\x1B\[[0-9;]*[a-zA-Z]', '', c)
    return re.sub(r'\x1B\[\?[0-9]*[a-zA-Z]', '', c)

def get_credits(filepath):
    if not os.path.exists(filepath): return 0
    content = clean_ansi(open(filepath).read())
    m = re.search(r'Credits: ([0-9.]+)', content)
    return float(m.group(1)) if m else 0

def check_fact(answer_text, question):
    """Ask LLM a binary YES/NO question about the answer."""
    prompt = f'Answer ONLY "YES" or "NO". Nothing else.\n\nGiven this answer:\n---\n{answer_text[:6000]}\n---\n\nQuestion: {question}\n\nAnswer (YES or NO only):'
    result = subprocess.run(
        ['kiro-cli', 'chat', '--no-interactive', '--trust-tools='],
        input=prompt, capture_output=True, text=True, timeout=60
    )
    output = clean_ansi(result.stdout)
    before_credits = output.split('Credits')[0] if 'Credits' in output else output
    return 'YES' in before_credits.upper()

results = {}
facts = json.load(open(FACTS_FILE))

# --- Countable Queries ---
print("=" * 60)
print("COUNTABLE QUERIES (Endpoint ID matching)")
print("=" * 60)

routers_file = os.path.join(WIKI_DIR, 'modules', 'routers.md')
routers = open(routers_file).read() if os.path.exists(routers_file) else ''
sections = re.split(r'^### ', routers, flags=re.MULTILINE)
q1_gt = set(re.findall(r'ep-(\d+)', [s for s in sections if s.startswith('repository')][0])) if routers else set()

countable_gts = {'1': q1_gt}
for q in ['5', '7', '10']:
    ea = os.path.join(QUERIES_DIR, f'q{q}', 'expected-answer.md')
    if os.path.exists(ea):
        countable_gts[q] = set(re.findall(r'ep-(\d+)', open(ea).read()))

print(f"\n{'Q':<4} {'Approach':<10} {'P':>6} {'R':>6} {'F1':>6} {'Credits':>8}")
print("-" * 50)

for q in ['1', '5', '7', '10']:
    if q not in countable_gts: continue
    gt = countable_gts[q]
    for approach, logfile in [('baseline', f'{RESULTS_DIR}/baseline/q{q}/full-log.txt'),
                               ('3stage', f'{RESULTS_DIR}/3stage/q{q}/stage2-log.txt')]:
        if not os.path.exists(logfile): continue
        content = clean_ansi(open(logfile).read())
        found = set(re.findall(r'ep-(\d+)', content))
        correct = found & gt
        p = len(correct)/len(found)*100 if found else 0
        r = len(correct)/len(gt)*100 if gt else 0
        f1 = 2*p*r/(p+r) if (p+r) else 0
        credits = get_credits(logfile)
        print(f"Q{q:<3} {approach:<10} {p:>5.1f}% {r:>5.1f}% {f1:>5.1f}% {credits:>7.2f}")
        results[f'q{q}_{approach}'] = {'type': 'countable', 'precision': round(p,1), 'recall': round(r,1), 'f1': round(f1,1), 'credits': credits}

# --- Narrative Queries (Fact-Checking) ---
print("\n" + "=" * 60)
print("NARRATIVE QUERIES (LLM Fact-Checking)")
print("=" * 60)
print(f"\n{'Q':<4} {'Approach':<10} {'R':>6} {'P':>6} {'F1':>6} {'Credits':>8}")
print("-" * 50)

for q in ['2', '3', '4', '6', '8', '9', '12', '13', '14', '15']:
    if f'q{q}' not in facts: continue
    qdata = facts[f'q{q}']
    
    for approach, logfile in [('baseline', f'{RESULTS_DIR}/baseline/q{q}/full-log.txt'),
                               ('3stage', f'{RESULTS_DIR}/3stage/q{q}/stage2-log.txt')]:
        if not os.path.exists(logfile): continue
        answer = clean_ansi(open(logfile).read())
        credits = get_credits(logfile)
        
        r_scores = []
        for fact in qdata['recall_facts']:
            try:
                r_scores.append(check_fact(answer, fact['question']))
            except:
                r_scores.append(False)
        
        p_scores = []
        for fact in qdata['precision_facts']:
            try:
                p_scores.append(not check_fact(answer, fact['question']))
            except:
                p_scores.append(True)
        
        recall = sum(r_scores)/len(r_scores)*100
        precision = sum(p_scores)/len(p_scores)*100
        f1 = 2*recall*precision/(recall+precision) if (recall+precision) else 0
        print(f"Q{q:<3} {approach:<10} {recall:>5.0f}% {precision:>5.0f}% {f1:>5.0f}% {credits:>7.2f}")
        results[f'q{q}_{approach}'] = {'type': 'narrative', 'recall': round(recall,1), 'precision': round(precision,1), 'f1': round(f1,1), 'recall_details': r_scores, 'precision_details': p_scores, 'credits': credits}

# --- Bug Localization ---
print("\n" + "=" * 60)
print("BUG LOCALIZATION (File matching)")
print("=" * 60)
print(f"\n{'Q':<4} {'Approach':<10} {'Result':<10} {'Credits':>8}")
print("-" * 40)

for q in range(16, 22):
    gt_file = os.path.join(QUERIES_DIR, f'q{q}', 'ground-truth.json')
    if not os.path.exists(gt_file): continue
    gt = json.load(open(gt_file))
    
    for approach, logfile in [('baseline', f'{RESULTS_DIR}/baseline/q{q}/full-log.txt'),
                               ('3stage', f'{RESULTS_DIR}/3stage/q{q}/stage2-log.txt')]:
        if not os.path.exists(logfile): continue
        content = clean_ansi(open(logfile).read())
        credits = get_credits(logfile)
        found = sum(1 for f in gt['files'] if f in content or f.split('/')[-1] in content)
        total = len(gt['files'])
        passed = found == total
        status = "✅ PASS" if passed else f"❌ {found}/{total}"
        print(f"Q{q:<3} {approach:<10} {status:<10} {credits:>7.2f}")
        results[f'q{q}_{approach}'] = {'type': 'localization', 'pass': passed, 'credits': credits}

# Save
output_file = os.path.join(EVAL_DIR, 'analysis', 'full-validation-results.json')
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\n✅ Results saved to: analysis/full-validation-results.json")
