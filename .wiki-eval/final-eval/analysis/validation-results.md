# Validation Results — F1 Score Calculations

This document shows how each F1 score in the paper was derived.

## Countable Queries (Endpoint Matching)

F1 = 2 × Precision × Recall / (Precision + Recall)

- Precision = correct endpoints found / total endpoints reported
- Recall = correct endpoints found / total endpoints in ground truth

### Q1: List all repo endpoints
- Ground truth: 200 endpoints (from modules/routers.md 'repository' section)
- 3-Stage found: 205 endpoint IDs
- Correct (intersection): 200
- Precision: 200/205 = 97.6%
- Recall: 200/200 = 100.0%
- **F1: 98.8%**

## Narrative Queries (Fact-Checking)

F1 = 2 × Recall × Precision / (Recall + Precision)

- Recall = recall facts answered YES / 10 total recall facts
- Precision = precision facts answered NO (no hallucination) / 5 total precision facts
- Each fact is a binary YES/NO question asked to the LLM about the answer

Fact definitions: [facts-checklist.json](../scripts/facts-checklist.json)

### Q2: If I need to add a new webhook event type, what files across...
- Recall facts: 10
- Precision facts: 5
- (Scores from final evaluation run — see results/3stage/q2/stage2-log.txt)

### Q3: What is the complete data flow when a user creates a pull re...
- Recall facts: 10
- Precision facts: 5
- (Scores from final evaluation run — see results/3stage/q3/stage2-log.txt)

### Q4: What are all the external services called during a repositor...
- Recall facts: 10
- Precision facts: 5
- (Scores from final evaluation run — see results/3stage/q4/stage2-log.txt)

### Q6: Document the complete permission checking chain for the repo...
- Recall facts: 10
- Precision facts: 5
- (Scores from final evaluation run — see results/3stage/q6/stage2-log.txt)

### Q8: Map the complete notification system: what events trigger no...
- Recall facts: 10
- Precision facts: 5
- (Scores from final evaluation run — see results/3stage/q8/stage2-log.txt)

### Q9: If the database connection pool is exhausted, which API endp...
- Recall facts: 10
- Precision facts: 5
- (Scores from final evaluation run — see results/3stage/q9/stage2-log.txt)

## Bug Localization (File Matching)

Score: Binary — does the answer contain the ground truth file path?

### Q16
- Ground truth files: ['routers/api/v1/api.go']
- Found in answer: ✅ YES
- Source: [ground-truth.json](../queries/q16/ground-truth.json)

### Q17
- Ground truth files: ['services/convert/convert.go']
- Found in answer: ✅ YES
- Source: [ground-truth.json](../queries/q17/ground-truth.json)

### Q18
- Ground truth files: ['routers/api/v1/repo/pull.go']
- Found in answer: ✅ YES
- Source: [ground-truth.json](../queries/q18/ground-truth.json)

### Q19
- Ground truth files: ['services/context/permission.go']
- Found in answer: ✅ YES
- Source: [ground-truth.json](../queries/q19/ground-truth.json)

### Q20
- Ground truth files: ['routers/api/v1/packages/package.go']
- Found in answer: ✅ YES
- Source: [ground-truth.json](../queries/q20/ground-truth.json)

### Q21
- Ground truth files: ['routers/api/v1/api.go']
- Found in answer: ✅ YES
- Source: [ground-truth.json](../queries/q21/ground-truth.json)
