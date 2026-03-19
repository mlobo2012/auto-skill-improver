# Worked Example — Social Post Style Skill

## Scenario
A social-post skill strongly prefers long-form bullet posts, but users sometimes ask for short one-liners or reply-style posts. The skill does not define how to switch modes.

## Hypothesis
A two-mode output contract will improve consistency:
- Mode A: long-form breakdown
- Mode B: short-form atomic post

## Benchmark
### Train prompts
- Write a short post about a surprising product choice.
- Draft a longer breakdown post with 3 bullet-style points.
- Write a reply-style take under 180 characters.

### Held-out prompt
- Write a concise builder-style post about a technical trade-off without hype language.

### Binary evals
- matches requested mode
- preserves required structure
- avoids banned phrases
- ends with a statement

## Baseline finding
The baseline handled long-form prompts well but forced long-form structure onto short prompts.

## Mutation
Add explicit mode-selection logic:
- use Mode B when the request asks for short, reply-style, concise, or under-N characters
- otherwise use Mode A

## Result
- Baseline: 62.5%
- Candidate: 87.5%

## Why this is a real improvement
The change resolves an actual ambiguity in the skill's decision logic instead of just adding more wording.

## Caveat
This benchmark tests structure and consistency, not real audience response.
