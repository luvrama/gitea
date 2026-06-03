# Final Evaluation — Pre-Compiled Wiki vs Baseline

## Architecture

```
Query → Classifier (LLM) → wiki: Page Selector (LLM) → Answerer (LLM, no tools)
                          → graph: LLM + graph_query tool → Answer
```

**Baseline:** LLM with full tool access (grep, read, glob) on raw source code.

## Folder Structure

```
final-eval/
├── scripts/                    # All prompts, tools, and runner
│   ├── run.sh                  # Main runner script
│   ├── prompt-classifier.md    # Stage 0: picks wiki or graph
│   ├── prompt-page-selector.md # Wiki path: selects pages + sections
│   ├── prompt-answerer.md      # Wiki path: answers from injected pages
│   ├── prompt-baseline.md      # Baseline: source code + tools
│   ├── prompt-graph-tool.md    # Graph path: LLM with graph_query tool
│   ├── graph_query.py          # Graph tool: queries pre-compiled knowledge graph
│   └── facts-checklist.json    # Validation: per-query fact definitions
├── queries/                    # Input: one folder per query
│   └── q{N}/
│       ├── prompt.txt          # The developer question
│       ├── expected-answer.md  # Ground truth (for narrative queries)
│       └── ground-truth.json   # Ground truth (for localization queries)
├── results/                    # Output: full logs per approach
│   ├── baseline/q{N}/
│   │   ├── prompt.md           # What was sent to LLM
│   │   └── full-log.txt        # Complete kiro-cli output
│   └── 3stage/q{N}/
│       ├── classification.txt  # "wiki" or "graph"
│       ├── stage0-log.txt      # Classifier output
│       ├── stage1-log.txt      # Page selection or graph query
│       ├── selected-pages.json # Pages selected (wiki path only)
│       └── stage2-log.txt      # Final answer
└── analysis/                   # Validation results + summary
    └── (generated after running)
```

## Usage

```bash
cd scripts/

# Run one query (both approaches):
./run.sh 1

# Run one approach only:
./run.sh 1 baseline
./run.sh 1 3stage

# Run all queries:
./run.sh all
```

## Query Categories

| Queries | Category | Validation Method |
|---------|----------|-------------------|
| Q1, Q5, Q7, Q10 | Enumeration (countable) | P/R/F1 by endpoint ID/path matching |
| Q2, Q3, Q4, Q6, Q8, Q9 | Flow/Architecture (narrative) | P/R/F1 by fact-checking |
| Q11-Q15 | Dependency/Graph | P/R/F1 by fact-checking |
| Q16-Q21 | Bug Localization (SWE-bench style) | File localization accuracy |
