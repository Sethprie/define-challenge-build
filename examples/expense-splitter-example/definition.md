# Definition: Expense Splitter

## 1. What it solves

A small group of people share expenses over a trip or a period of time. Each expense is paid up front by one person on behalf of some subset of the group. At the end, the group needs to know the smallest possible set of payments that settles everyone up.

## 2. Business rules

- Each expense has: a **payer**, an **amount**, and a **list of participants** (the people the expense is split among). The payer must always be included in the participants.
- Splits are **equal only** in this version — every participant owes the same share of the expense.
- Amounts are handled internally in **integer cents**, never floats, to avoid rounding drift.
- **Rounding rule:** when an amount doesn't divide evenly among participants, the leftover cent(s) are absorbed by the payer, not distributed among the group.
- The output is the **minimum practical number of transactions** that settles all balances — not a full history of who paid whom for what.
- If, after netting all expenses, a person's balance is exactly zero, they appear in no transaction.

## 3. Scope

- Single currency. No conversion, no currency field.
- Single run: the tool reads one CSV file of expenses and prints a settlement plan. No persistence between runs.
- Command-line only.

## 4. Out of scope

- Multi-currency support.
- Uneven / custom split ratios (e.g. 70/30).
- Persistence, accounts, or authentication.
- A guaranteed mathematically optimal minimum-transaction solution (that's an NP-hard set-partition problem) — a good practical heuristic is acceptable and must be documented as such.
