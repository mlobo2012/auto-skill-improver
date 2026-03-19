# Triage

Before you run a full optimization loop, do a fast triage.

## Step 1: Is this skill a good target?
Good targets:
- ambiguous formatting/content skills
- audit/research skills with weak evidence discipline
- execution skills with dependency or fallback problems
- systems with conflicting instruction layers

Weak targets:
- tiny reference skills
- already-crisp single-purpose skills
- skills without measurable outputs

## Step 2: Can you build a real benchmark?
If you cannot define 3-6 binary evals that matter to actual task success, stop.

## Step 3: Run a saturation pre-check
Use 2-3 prompts and a small eval set.
If the baseline already scores above 90%, tighten the benchmark or stop early.

## Step 4: Pick the pass depth
- quick pass: baseline + one mutation
- standard pass: baseline + 1-3 mutations + held-out check
- deep pass: only when the benchmark is strong and the skill is important

## Stop if
- the benchmark stays saturated
- the mutation cannot be isolated cleanly
- the evaluation is clearly circular and uninformative
- the skill is already good enough relative to the benchmark
