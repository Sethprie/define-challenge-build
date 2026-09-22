# Roadmap: Expense Splitting — Core

## 1. Definition

- **What it solves:** the calculation engine — turning a list of expenses into balances, then into a minimal settlement plan. Covers `definition.md` sections 2 and 4.
- **Scope:** pure logic, no I/O, no CLI. Consumes already-parsed rows; doesn't read files itself.

## 2. Phases and Tasks

### Phase 1: Data model and validation
- [ ] Define an `Expense` type with `payer`, `amount_cents`, and `participants`.
- [ ] Reject on construction: non-positive `amount_cents`, payer missing from `participants`, duplicate participants.

### Phase 2: Parsing
- [ ] Convert raw string rows (`payer`, `amount`, `participants` as a `;`-separated string) into `Expense` objects, converting the decimal amount into integer cents.

### Phase 3: Balance calculation
- [ ] For each expense, credit the payer the full amount and debit each participant their equal share.
- [ ] Any rounding remainder from an uneven split is added to the payer's share, per `definition.md` section 2.
- [ ] Produce one net balance (in cents) per person: positive means owed money, negative means owes money.

### Phase 4: Settlement
- [ ] Implement a greedy algorithm: repeatedly match the largest creditor with the largest debtor until every balance reaches zero.
- [ ] Document inline that this is a practical heuristic, not a guaranteed minimum — acceptable per `definition.md` section 4.
- [ ] People whose net balance is already zero produce no transaction.
