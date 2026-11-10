# Examples

Real output from BudgetPlan, captured from actual runs.

## Default 50/30/20 split

Command:

```bash
python3 budgetplan.py --income 2000
```

Output:

```
Income: 2000.00
Needs (50%): 1000.00
  Rent, bills, groceries, transport.
Wants (30%): 600.00
  Eating out, fun, subscriptions.
Savings and debt payoff (20%): 400.00
  Emergency fund first, then goals.
Per year: needs 12000.00, wants 7200.00, savings 4800.00
```

## Custom split, saved to CSV

Command:

```bash
python3 budgetplan.py --income 2000 --needs 60 --wants 20 --savings 20 --out /tmp/plan.csv
```

Output:

```
Income: 2000.00
Needs (60%): 1200.00
  Rent, bills, groceries, transport.
Wants (20%): 400.00
  Eating out, fun, subscriptions.
Savings and debt payoff (20%): 400.00
  Emergency fund first, then goals.
Per year: needs 14400.00, wants 4800.00, savings 4800.00
Plan saved to /tmp/plan.csv
```

The saved CSV file (`/tmp/plan.csv`) contains:

```
bucket,percent,amount
Needs,60,1200.00
Wants,20,400.00
Savings and debt payoff,20,400.00
```
