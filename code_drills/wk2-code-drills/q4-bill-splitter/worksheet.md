# Q4 — Restaurant Bill Splitter

**Topic:** Input, Mixed Types, Arithmetic | **Week 2** | **Difficulty:** Easy-Medium (~4 marks)

---

## Skills Practiced

| Skill | Lecture |
|-------|---------|
| `float()` vs `int()` cast | 2-1E |
| Arithmetic: `*`, `/`, `+` | Week 1 |
| `.format()` with `:.2f` | 2-1B |

---

## Problem

A group of friends wants to split a restaurant bill evenly, including a tip.

Write a program that:
1. Asks for the total bill ($), number of people, and tip percentage
2. Calculates the tip amount, grand total, and each person's share
3. Displays all three values to 2 decimal places

---

## Sample Runs

**Sample 1**
```
Enter total bill ($)    : 80
Enter number of people  : 4
Enter tip percentage    : 10
Tip amount  : $8.00
Grand total : $88.00
Per person  : $22.00
```

**Sample 2**
```
Enter total bill ($)    : 65.50
Enter number of people  : 3
Enter tip percentage    : 15
Tip amount  : $9.82
Grand total : $75.33
Per person  : $25.11
```

**Sample 3**
```
Enter total bill ($)    : 120
Enter number of people  : 6
Enter tip percentage    : 12
Tip amount  : $14.40
Grand total : $134.40
Per person  : $22.40
```

---

## Guided Questions

**1.** Which type should `num_people` be? Why not `float`?

> _________________________________________________________________

**2.** Write the formula for `tip_amount`:

> `tip_amount = _______________`

**3.** Write the formula for `per_person`:

> `per_person = _______________`

**4.** Trace Sample 1 manually. Fill in the blanks:

| Variable | Calculation | Value |
|----------|-------------|-------|
| `tip_amount` | 80 × 10 ÷ 100 | `_____` |
| `grand_total` | 80 + _____ | `_____` |
| `per_person` | _____ ÷ 4 | `_____` |

---

## Common Mistakes

1. **Using `int()` for the bill** — `int("65.50")` raises a `ValueError`. Bills can be decimals; use `float()`.
2. **Computing tip as a decimal directly** — if the user enters `10` (meaning 10%), you need to divide by 100 in the formula: `total_bill * tip_pct / 100`, not `total_bill * tip_pct`.
3. **Dividing by `float` people** — `int(input(...))` for `num_people` is correct. Python 3 division with `/` always returns a float, so `88.00 / 4` gives `22.0` without issue.
4. **Rounding before the final calculation** — always compute with the full precision value. Only format with `:.2f` at the print step.
