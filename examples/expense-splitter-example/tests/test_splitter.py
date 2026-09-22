import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from splitter import Expense, compute_balances, settle  # noqa: E402


def test_equal_split_two_people():
    expenses = [Expense(payer="ana", amount_cents=1000, participants=("ana", "bob"))]
    balances = compute_balances(expenses)
    assert balances == {"ana": 500, "bob": -500}

    transactions = settle(balances)
    assert transactions == [("bob", "ana", 500)]


def test_rounding_remainder_goes_to_payer():
    # 1001 cents split three ways: 333 each, 2 cents remainder -> payer keeps it
    expenses = [Expense(payer="ana", amount_cents=1001, participants=("ana", "bob", "cara"))]
    balances = compute_balances(expenses)
    assert balances["bob"] == -333
    assert balances["cara"] == -333
    assert balances["ana"] == 666  # owed 1001, owes 335 (333 + 2 remainder)


def test_everyone_already_settled_produces_no_transactions():
    balances = {"ana": 0, "bob": 0}
    assert settle(balances) == []


def test_rejects_non_positive_amount():
    try:
        Expense(payer="ana", amount_cents=0, participants=("ana", "bob"))
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for zero amount")


def test_rejects_payer_not_in_participants():
    try:
        Expense(payer="ana", amount_cents=500, participants=("bob", "cara"))
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for missing payer")


if __name__ == "__main__":
    test_equal_split_two_people()
    test_rounding_remainder_goes_to_payer()
    test_everyone_already_settled_produces_no_transactions()
    test_rejects_non_positive_amount()
    test_rejects_payer_not_in_participants()
    print("All tests passed.")
