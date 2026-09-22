"""Core logic for the expense splitter.

Implements: roadmaps/roadmap-splitting/roadmap-splitting-core.md
"""
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Expense:
    payer: str
    amount_cents: int
    participants: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.amount_cents <= 0:
            raise ValueError(f"expense amount must be positive, got {self.amount_cents}")
        if self.payer not in self.participants:
            raise ValueError(f"payer '{self.payer}' must be included in participants")
        if len(set(self.participants)) != len(self.participants):
            raise ValueError("participants must not contain duplicates")


def parse_expenses(rows: Iterable[dict[str, str]]) -> list[Expense]:
    """Turn parsed CSV rows into Expense objects.

    Expected columns: payer, amount, participants (';'-separated names).
    Amounts are decimal strings (e.g. "12.50") and are converted to
    integer cents here so the rest of the pipeline never touches floats.
    """
    expenses: list[Expense] = []
    for row in rows:
        amount_cents = round(float(row["amount"]) * 100)
        participants = tuple(p.strip() for p in row["participants"].split(";") if p.strip())
        expenses.append(
            Expense(payer=row["payer"].strip(), amount_cents=amount_cents, participants=participants)
        )
    return expenses


def compute_balances(expenses: Iterable[Expense]) -> dict[str, int]:
    """Return each person's net balance in cents.

    Positive balance: is owed money. Negative balance: owes money.
    Any leftover cent from an uneven equal split is absorbed by the
    payer, per definition.md section 2 ("Rounding rule").
    """
    balances: dict[str, int] = {}

    def add(person: str, delta: int) -> None:
        balances[person] = balances.get(person, 0) + delta

    for expense in expenses:
        share = expense.amount_cents // len(expense.participants)
        remainder = expense.amount_cents - share * len(expense.participants)

        add(expense.payer, expense.amount_cents)
        for participant in expense.participants:
            owed = share
            if participant == expense.payer:
                owed += remainder
            add(participant, -owed)

    return balances


def settle(balances: dict[str, int]) -> list[tuple[str, str, int]]:
    """Greedy settlement: repeatedly match the largest creditor with the
    largest debtor until every balance is zero.

    NOTE: this is a practical heuristic, not a guaranteed minimum number
    of transactions. Finding the true minimum is an NP-hard set-partition
    problem. This trade-off is accepted in definition.md section 4 and
    recorded in roadmaps/roadmap-splitting/challenge-log.md.
    """
    creditors = [[person, amount] for person, amount in balances.items() if amount > 0]
    debtors = [[person, -amount] for person, amount in balances.items() if amount < 0]
    creditors.sort(key=lambda x: -x[1])
    debtors.sort(key=lambda x: -x[1])

    transactions: list[tuple[str, str, int]] = []
    i = j = 0
    while i < len(debtors) and j < len(creditors):
        debtor, debt = debtors[i]
        creditor, credit = creditors[j]
        payment = min(debt, credit)
        if payment > 0:
            transactions.append((debtor, creditor, payment))

        debtors[i][1] -= payment
        creditors[j][1] -= payment

        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    return transactions
