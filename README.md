
# $ Expense Tracker $

A simple Python script to track and visualize your expenses from a bank CSV statement.

---

## Features

* Reads and cleans CSV bank data
* Categorizes expenses into `food`, `travel`, `shopping`, `stay`, `bills`, or `others`
* Detects `zelle` and names as bill payments
* Shows total spending by category
* Generates a pie chart (`category_spending_pie.png`)

---

## How to Use

1. Place your bank CSV as `BankStatement.csv`
2. Run the script:

```bash
python Extracker.py
```

3. See results in the terminal and view the pie chart

---

## Requirements : 

```bash
pip install pandas matplotlib
```

---

## Customize

Edit the `data` dictionary in the script to change category keywords.
