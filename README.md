# Auto Skill Improver

> Most prompt iteration is theater. This is how you stop lying to yourself about whether anything got better.

Auto Skill Improver is a **benchmark-first loop** for improving Claude Code, Cowork, and OpenClaw skills through controlled mutation and honest keep/discard decisions — not prompt vibes.

It is built for people who have real skill files or prompt specs and want to know — with evidence — whether a change actually made things better.

---

## The Problem

The failure mode is always the same.

You mutate an instruction. You read the new version. It sounds more sophisticated, so you keep it. Nothing measurably improved.

Auto Skill Improver resists that trap by treating skill iteration as an empirical process, not an editorial one.

---

## The Benchmark-Mutation Loop

The core method — directly inspired by Andrej Karpathy's autoresearch work — applies the same measurement discipline to skill files and prompt specs:

1. **Classify** the skill type
2. **Build a benchmark** that can actually distinguish success from failure
3. **Establish a baseline** before you change anything
4. **Mutate one thing** at a time
5. **Keep only what improves the score**
6. **Stop** when the benchmark saturates or stops teaching you anything

The principle we borrowed from Karpathy is not "let an AI improve itself." It is the more disciplined idea underneath it: use a bounded environment, a real benchmark, a repeatable loop, and make decisions based on evidence — not instinct.

---

## Where It Works Best

Auto Skill Improver produces real signal on skills with:

- **Ambiguous output contracts** — the skill doesn't clearly define what good looks like
- **Missing fallback behavior** — the skill collapses when a dependency is unavailable
- **Conflicting instruction layers** — one rule contradicts another
- **Dependency or portability problems** — the skill breaks outside its original environment
- **Weak evidence discipline** — the skill invents certainty when data is missing
- **Structural formatting rules** — output shape can be checked programmatically

### Worked examples

**Missing fallback:** A skill relies on a reference file for its core quality check. If the file is missing, the skill's main promise collapses. A fallback mutation produces a real, testable improvement.

**Conflicting rules:** One skill says "close with a statement" while another encourages question endings. Adding an explicit priority rule is a real, measurable change.

**Benchmark saturation:** A compact reference skill that already lists the necessary commands may saturate the benchmark immediately. The right answer is to stop — and that is still useful information.

---

## Where It Does Not Fit

Be realistic about scope.

Auto Skill Improver is a poor fit when:

- The skill is already small, crisp, and adequate
- The only thing you care about is subjective taste
- You cannot build a meaningful benchmark
- The benchmark saturates immediately and tightening does not help
- The target is a high-risk orchestration layer without proxy metrics

It can surface missing decision logic, broken dependencies, contradictory instructions, and weak output contracts. It cannot solve taste, deep product judgment, audience resonance, or real-world performance without real-world testing.

---

## What It Finds

- Missing decision logic
- Broken dependencies
- Contradictory instructions
- Weak output contracts
- Evaluator saturation

## What It Cannot Fix

- Taste
- Deep product judgment
- Audience resonance
- Real-world performance without real-world testing

---

## How To Use It

1. Read `docs/TRIAGE.md`
2. Pick a target skill
3. Classify the skill type
4. Build a small benchmark
5. Run a baseline — **before you change anything**
6. Tighten the benchmark if it saturates immediately
7. Mutate one thing
8. Re-run and review the diff
9. Keep or discard honestly

---

## Honest Limitations

Same-model evaluation can be circular. Formatting quality is hard to measure with binary checks alone. Some skills require proxy benchmarks rather than direct scoring. Portability improvements can conflict with platform-specific optimization.

Read `docs/LIMITATIONS.md` before treating any score as definitive.

A binary eval can still be useless. The goal is not just yes/no questions — it is yes/no questions tied to task success.

---

## UX and Run Model

The best UX for Auto Skill Improver is a **research-run workflow**, not a live dashboard.

Users should stay in the loop through decision checkpoints:
- baseline complete
- benchmark saturated
- mutation kept
- regression detected
- final summary ready

Best default mode:
- supervised batch run
- baseline + 1-3 mutations + summary + human decision

Best operational trigger:
- run on skill changes, model changes, repeated failures, or dependency breakage
- do not run blind timer-based optimization on everything

Read:
- `docs/UX-MODEL.md`
- `docs/RUN-MODES.md`

## Repo Structure

```text
skills/       — optimizer specs for different execution environments
docs/         — limitations, triage, eval patterns, context intake, and run guidance
harnesses/    — public-safe template harnesses
examples/     — synthetic worked examples
```

---

## Key Principles

- If you mutate before measuring the starting point, you are doing theater, not research.
- If you change five things at once, you lose attribution.
- If the baseline already scores near-perfectly, your skill may already be good — or your benchmark is weak. Either way, do not claim improvement.
- Longer loops are not always better loops.
- **The point is not to make skills longer. The point is to make them clearer, more robust, and more measurably useful.**
- If the benchmark says nothing improved, that is still useful information.

---

## License

MIT
