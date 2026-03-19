# UX Model

Auto Skill Improver is not designed to be a live dashboard toy. It is designed to be a research-run workflow.

## Core UX principle
Users should stay in the loop through **decision checkpoints**, not constant surveillance.

## What the user needs to see
At any given time, the user mainly needs three things:

1. **What is being tested**
   - target skill
   - benchmark design
   - baseline result
   - current candidate

2. **Whether the loop is learning anything**
   - score changes
   - failing evals
   - saturation warnings
   - regression guards

3. **What decision is being recommended**
   - keep
   - discard
   - tighten benchmark
   - stop
   - human review

## Recommended UX artifacts
A good run should produce:
- `baseline.md`
- `candidate.md`
- `results.tsv`
- `results.json`
- `changelog.md`
- `summary.md`

## Best notification moments
Notify the user when:
- baseline is complete
- the benchmark is saturated
- a mutation is kept
- a regression is detected
- the run is complete

Do **not** notify on every tiny internal step.

## Default experience
The best default is a **supervised batch run**:
- baseline
- 1-3 mutations
- summary
- human decision

This is better than an open-ended always-on loop for most skills.
