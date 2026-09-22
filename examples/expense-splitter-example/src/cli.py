"""Command-line interface for the expense splitter.

Implements: roadmaps/roadmap-splitting/roadmap-splitting-cli.md
"""
import argparse
import csv
import sys

from splitter import compute_balances, parse_expenses, settle


def format_cents(cents: int) -> str:
    return f"{cents / 100:.2f}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Split shared expenses and print who owes whom.")
    parser.add_argument("csv_path", help="Path to a CSV file with columns: payer,amount,participants")
    args = parser.parse_args(argv)

    try:
        with open(args.csv_path, newline="", encoding="utf-8") as f:
            expenses = parse_expenses(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        return 1
    except (KeyError, ValueError) as exc:
        print(f"Error: invalid data in {args.csv_path}: {exc}", file=sys.stderr)
        return 1

    if not expenses:
        print("No expenses to settle.")
        return 0

    balances = compute_balances(expenses)
    transactions = settle(balances)

    if not transactions:
        print("Everyone is already settled up.")
        return 0

    for debtor, creditor, amount in transactions:
        print(f"{debtor} pays {creditor}: {format_cents(amount)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
