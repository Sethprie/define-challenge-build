# Challenge Log — roadmap-splitting

Audited using `prompts/challenge/roadmap-challenge.md`, once per roadmap file.

## roadmap-splitting-core.md

**Finding 1 — Greedy settlement isn't provably minimal.**
Flagged that the greedy largest-creditor/largest-debtor match is a heuristic, not a guaranteed minimum, and asked whether that's acceptable.
*Resolution:* accepted as-is — `definition.md` section 4 already allows a documented heuristic instead of a guaranteed optimum. Added an explicit inline-documentation task to Phase 4 so this trade-off is visible in the code, not just in this log.

**Finding 2 — Duplicate participants weren't validated.**
The first draft of the roadmap didn't mention rejecting duplicate names in the participants list, which would silently double-count someone's share.
*Resolution:* added to Phase 1 as an explicit validation rule.

## roadmap-splitting-cli.md

**Finding 1 — Errors printed to stdout.**
The first draft said errors should be "printed", without specifying the stream, which risked mixing error text with normal output.
*Resolution:* Phase 2 now explicitly says errors go to stderr with a non-zero exit code.

No objections remained after these fixes. Both roadmaps consolidated.
