# When Not to Use Auto Skill Improver

Do not use this just because you can.

## Avoid or deprioritize when
- the skill is tiny and already clear
- the likely mutation is just prompt mass
- you cannot define a meaningful benchmark
- the only thing you care about is subjective taste
- the target is high-risk and you have no proxy metrics

## Warning signs
- the baseline saturates immediately
- tightening the benchmark still does not discriminate
- the model starts gaming the eval wording
- the skill keeps getting longer without becoming more useful

## Better fits
- broken fallback behavior
- conflicting instruction layers
- weak output contracts
- invented certainty in audit-style outputs
- dependency-sensitive skills
