# BudgetPlan

Split your monthly income into a simple needs, wants and savings plan in one command.

BudgetPlan is built on the 50/30/20 idea: about 50% of take-home pay goes to needs, 30% to wants, and 20% to savings and debt payoff.
It prints the monthly amount for each bucket, what that bucket is for, the yearly totals, and can save the plan as CSV — and you can change the split to any percents that add up to 100.

## Requirements

- Python 3
- Standard library only — nothing to install

## Usage

Default 50/30/20 split on a monthly income of 2000:

```bash
python3 budgetplan.py --income 2000
```

Custom 60/20/20 split, also saved to a CSV file:

```bash
python3 budgetplan.py --income 2000 --needs 60 --wants 20 --savings 20 --out plan.csv
```

## Options

| Option | Meaning | Default |
|---|---|---|
| `--income` | Monthly take-home income (required) | — |
| `--needs` | Percent for needs | 50 |
| `--wants` | Percent for wants | 30 |
| `--savings` | Percent for savings and debt payoff | 20 |
| `--out` | Optional CSV path to save the plan | — |

The three percents must add up to exactly 100; if they do not, the tool
stops with a clear error showing the actual sum.

See `examples.md` for real captured output.

## License

MIT — see `LICENSE`.
