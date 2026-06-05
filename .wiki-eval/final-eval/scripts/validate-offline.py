#!/usr/bin/env python3
"""
validate-offline.py — Offline validation (no LLM required)
Computes P/R/F1 for countable queries and pass/fail for bug localization.
Uses only files in this repo.

Usage: python3 validate-offline.py
"""
import json, re, os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EVAL_DIR = os.path.dirname(SCRIPT_DIR)
RESULTS_DIR = os.path.join(EVAL_DIR, 'results')
QUERIES_DIR = os.path.join(EVAL_DIR, 'queries')
WIKI_DIR = os.path.join(os.path.dirname(os.path.dirname(EVAL_DIR)), '.project-analysis', 'wiki')

def clean_ansi(c):
    c = re.sub(r'\x1B\[[0-9;]*[a-zA-Z]', '', c)
    return re.sub(r'\x1B\[\?[0-9]*[a-zA-Z]', '', c)

def get_credits(filepath):
    if not os.path.exists(filepath): return 0
    content = clean_ansi(open(filepath).read())
    m = re.search(r'Credits: ([0-9.]+)', content)
    return float(m.group(1)) if m else 0

results = {}

# --- Countable Queries (Q1, Q5, Q7, Q10) ---
print("=" * 60)
print("COUNTABLE QUERIES (Endpoint ID matching)")
print("=" * 60)

# Load ground truths
routers_file = os.path.join(WIKI_DIR, 'modules', 'routers.md')
if os.path.exists(routers_file):
    routers = open(routers_file).read()
    sections = re.split(r'^### ', routers, flags=re.MULTILINE)
    q1_gt = set(re.findall(r'ep-(\d+)', [s for s in sections if s.startswith('repository')][0]))
else:
    q1_gt = set()

countable_gts = {'1': q1_gt}
for q in ['5', '7', '10']:
    ea = os.path.join(QUERIES_DIR, f'q{q}', 'expected-answer.md')
    if os.path.exists(ea):
        countable_gts[q] = set(re.findall(r'ep-(\d+)', open(ea).read()))

print(f"\n{'Q':<4} {'Approach':<10} {'Found':<7} {'Correct':<9} {'P':>6} {'R':>6} {'F1':>6} {'Credits':>8}")
print("-" * 60)

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
        print(f"Q{q:<3} {approach:<10} {len(found):<7} {len(correct):<9} {p:>5.1f}% {r:>5.1f}% {f1:>5.1f}% {credits:>7.2f}")
        results[f'q{q}_{approach}_countable'] = {
            'precision': round(p, 1), 'recall': round(r, 1), 'f1': round(f1, 1), 'credits': credits
        }

# --- Bug Localization (Q16-Q21) ---
print("\n" + "=" * 60)
print("BUG LOCALIZATION (File matching)")
print("=" * 60)
print(f"\n{'Q':<4} {'Approach':<10} {'Result':<10} {'Credits':>8} {'Ground Truth Files'}")
print("-" * 70)

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
        print(f"Q{q:<3} {approach:<10} {status:<10} {credits:>7.2f}  {gt['files']}")
        results[f'q{q}_{approach}_localization'] = {
            'pass': passed, 'files_found': found, 'files_total': total, 'credits': credits
        }

# --- Cost Summary ---
print("\n" + "=" * 60)
print("COST SUMMARY (All 21 Queries)")
print("=" * 60)

baseline_total = 0
threestage_total = 0
for q in range(1, 22):
    b = get_credits(f'{RESULTS_DIR}/baseline/q{q}/full-log.txt')
    s = sum(get_credits(f'{RESULTS_DIR}/3stage/q{q}/{f}') for f in ['stage0-log.txt', 'stage1-log.txt', 'stage2-log.txt'])
    baseline_total += b
    threestage_total += s

print(f"\n  Baseline total:  {baseline_total:.2f} credits (avg: {baseline_total/21:.2f})")
print(f"  3-Stage total:   {threestage_total:.2f} credits (avg: {threestage_total/21:.2f})")
print(f"  Cost reduction:  {(1 - threestage_total/baseline_total)*100:.0f}%")

# Save results
output_file = os.path.join(EVAL_DIR, 'analysis', 'validation-offline-results.json')
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\n✅ Results saved to: analysis/validation-offline-results.json")
