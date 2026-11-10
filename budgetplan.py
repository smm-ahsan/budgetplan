#!/usr/bin/env python3
"""BudgetPlan - split monthly income into a simple needs/wants/savings plan.

Uses the classic 50/30/20 budgeting idea by default: 50% of take-home pay
for needs, 30% for wants, 20% for savings and debt payoff. The split is
fully adjustable as long as the three percents add up to 100.

Standard library only.
"""

import argparse
import csv
import sys

BUCKET_NOTES = {
    "Needs": "Rent, bills, groceries, transport.",
    "Wants": "Eating out, fun, subscriptions.",
    "Savings and debt payoff": "Emergency fund first, then goals.",
}


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Split monthly income into a simple budget plan."
    )
    parser.add_argument(
        "--income",
        type=float,
        required=True,
        help="Monthly take-home income (required).",
    )
    parser.add_argument(
        "--needs",
        type=float,
        default=50,
        help="Percent of income for needs (default: 50).",
    )
    parser.add_argument(
        "--wants",
        type=float,
        default=30,
        help="Percent of income for wants (default: 30).",
    )
    parser.add_argument(
        "--savings",
        type=float,
        default=20,
        help="Percent of income for savings and debt payoff (default: 20).",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Optional path to also save the plan as a CSV file.",
    )
    return parser.parse_args(argv)


def fmt_percent(p):
    """Render a percent without a trailing .0 when it is a whole number."""
    if float(p).is_integer():
        return str(int(p))
    return f"{p:g}"


def main(argv=None):
    args = parse_args(argv)

    if args.income <= 0:
        print(
            f"error: --income must be greater than 0 (got {args.income})",
            file=sys.stderr,
        )
        return 2

    total = args.needs + args.wants + args.savings
    if abs(total - 100) > 0.001:
        print(
            "error: --needs + --wants + --savings must add up to 100 "
            f"(got {total:g}: needs {fmt_percent(args.needs)} + "
            f"wants {fmt_percent(args.wants)} + "
            f"savings {fmt_percent(args.savings)})",
            file=sys.stderr,
        )
        return 2

    buckets = [
        ("Needs", args.needs),
        ("Wants", args.wants),
        ("Savings and debt payoff", args.savings),
    ]
    amounts = [(name, pct, args.income * pct / 100.0) for name, pct in buckets]

    print(f"Income: {args.income:.2f}")
    for name, pct, amount in amounts:
        print(f"{name} ({fmt_percent(pct)}%): {amount:.2f}")
        print(f"  {BUCKET_NOTES[name]}")

    yearly = {name: amount * 12 for name, _, amount in amounts}
    print(
        "Per year: needs {n:.2f}, wants {w:.2f}, savings {s:.2f}".format(
            n=yearly["Needs"],
            w=yearly["Wants"],
            s=yearly["Savings and debt payoff"],
        )
    )

    if args.out:
        with open(args.out, "w", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["bucket", "percent", "amount"])
            for name, pct, amount in amounts:
                writer.writerow([name, fmt_percent(pct), f"{amount:.2f}"])
        print(f"Plan saved to {args.out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
