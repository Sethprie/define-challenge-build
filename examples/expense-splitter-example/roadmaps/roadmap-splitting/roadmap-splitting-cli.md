# Roadmap: Expense Splitting — CLI

## 1. Definition

- **What it solves:** the command-line interface — reading the input CSV, calling the core engine, and printing the settlement plan. Covers `definition.md` section 3 ("command-line only", "reads one CSV file").
- **Scope:** I/O and presentation only. No splitting or balancing logic lives here.

## 2. Phases and Tasks

### Phase 1: Argument parsing
- [ ] Accept a single required positional argument: the path to the expenses CSV.

### Phase 2: File reading
- [ ] Read the CSV with columns `payer,amount,participants` and hand the rows to the core parser.
- [ ] On a missing file, print a clear error to stderr and exit with a non-zero status.
- [ ] On malformed rows (missing column, invalid amount, validation errors from the core), print a clear error to stderr and exit with a non-zero status — do not print a partial result.

### Phase 3: Output formatting
- [ ] If there are no expenses, print "No expenses to settle."
- [ ] If everyone already nets to zero, print "Everyone is already settled up."
- [ ] Otherwise print one line per transaction: `<debtor> pays <creditor>: <amount>`, amount formatted with two decimals.
