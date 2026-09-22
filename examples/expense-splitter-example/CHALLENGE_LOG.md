# Challenge Log — Definition

Audited using `prompts/challenge/define-challenge.md` against an early draft of `definition.md`.

## Round 1

**Finding 1 — Invalid amounts not addressed.**
The draft didn't say what happens with a zero or negative expense amount.
*Fix:* added to section 2 (implicitly enforced at parse time in the core roadmap) — any non-positive amount is rejected as invalid input.

**Finding 2 — Floating point risk.**
The draft described amounts as plain decimals with no mention of how they're stored internally, which risks floating-point rounding errors accumulating across many expenses.
*Fix:* added "amounts are handled internally in integer cents" to section 2.

**Finding 3 — Rounding remainder undefined.**
When an expense doesn't divide evenly among participants, the draft didn't say who absorbs the leftover cent(s).
*Fix:* added the rounding rule to section 2 — the payer absorbs the remainder.

**Finding 4 — "Minimum number of transactions" is ambiguous.**
The draft said the tool "minimizes transactions" without saying whether that's a guaranteed mathematical minimum or a heuristic. This matters because the guaranteed minimum is NP-hard in the general case.
*Fix:* clarified in section 4 (Out of scope) that a documented heuristic is acceptable — the exact algorithm and its limitation are then specified in the Roadmap, not the Definition, since that's an implementation detail.

No objections remained after these fixes. Definition consolidated.
