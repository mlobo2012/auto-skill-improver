---
name: auto-skill-improver-claude-code
description: "Claude Code-compatible workflow for improving skills through baseline benchmarking, one-change mutation loops, and honest keep/discard decisions."
---

# Auto Skill Improver (Claude Code-compatible)

Use this workflow to improve a real `SKILL.md` file through empirical iteration.

## Core rule
Never mistake better-sounding skill text for better task performance.
Measure downstream behavior whenever possible.

## Required setup
Before running:
- identify target `SKILL.md`
- classify the skill type
- define train prompts and held-out prompts
- define 3-6 binary evals on outputs or operational behavior
- define candidate working copy name
- define stopping rules and run budget

If these are missing, stop and gather them.

## Skill type categories
Classify the target skill before building the benchmark. Choose the most specific one:
- execution
- routing
- artifact
- formatting/content
- research/audit
- meta-skill

Write down the classification explicitly and build the evaluator accordingly.

## Experiment protocol

### 1. Read the target skill fully
Also read any referenced files that materially define behavior.
Document:
- trigger conditions
- required tools/backends
- output contract
- fallback behavior
- anti-patterns
- ambiguity or conflicts

### 2. Build the benchmark harness
The harness must transform each test prompt into a measurable result.
Prefer:
- executed commands
- rendered artifacts
- parsed outputs
- validated structures
- source-backed analysis

Use text-only scoring only when no stronger operationalization exists.

### 3. Establish baseline
Create a safe candidate copy and run the untouched baseline first.
Record total score, per-eval pass counts, and failure examples.

### 4. Run saturation check
If baseline saturates the benchmark, the benchmark is weak.
Tighten evals, increase grounding, or add held-out prompts.
Do not claim improvement on a saturated benchmark.

### 5. Mutate one thing
Change exactly one thing at a time.

Good changes:
- clarify one priority
- add one missing fallback
- add one anti-pattern
- move a buried instruction up
- add one high-signal example
- remove one conflicting rule

Bad changes:
- multi-change rewrites
- evaluator-gaming language
- verbosity without test-backed reason

### 6. Re-run benchmark
Use the same train prompts and the same held-out prompts.

### 7. Keep or discard
- better on train and not worse on held-out -> keep
- same score -> discard unless materially simpler
- worse or overfit -> discard

### 8. Log everything
For each experiment write:
- hypothesis
- exact change
- score delta
- failures fixed
- failures introduced
- keep/discard decision

### 9. Review the diff (mandatory)
Before accepting a kept mutation, review the diff between baseline and candidate.
Check for:
- hidden regressions
- stale cross-references
- shortcut risk
- loss of tool guidance or safety caveats
- accidental multi-change mutations

## Deliverables
Create:
- improved candidate skill file
- baseline copy
- benchmark harness script(s)
- results log
- changelog
- concise summary of what improved and what remains weak

## Hard truth
Most skill-optimization failures are evaluator failures.
If the run says everything improved but real task quality did not, the benchmark is wrong.
Fix the benchmark before mutating more.

## Limitations
- Same-model evaluation is often circular; treat results as directional unless grounded in execution, dependencies, or real downstream effects.
- Formatting/content skills are harder to benchmark honestly than execution or dependency-fix skills.
- If the benchmark saturates or cannot discriminate after tightening, stop early.
- Do not use this protocol reflexively on tiny, already-crisp skills.
