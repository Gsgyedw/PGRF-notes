# Q7 — Stall Price Category

**Topic:** if/elif/else Chain | **Week 3** | **Difficulty:** Easy-Medium (~5 marks)

---

## Skills Practiced

| Skill | Lecture |
|-------|---------|
| `if` / `elif` / `else` chain | 3-2B |
| 3-way classification with ordered thresholds | 3-2B |
| `float()` input cast | 2-1E |

---

## Problem

FoodClub OS classifies each stall into a price category based on its **average meal price**.

| Average Price | Category |
|--------------|----------|
| Less than $4.00 | Budget |
| $4.00 to less than $7.00 | Standard |
| $7.00 and above | Premium |

Write a program that asks for the average meal price and prints the category.

---

## Sample Runs

**Sample 1**
```
Enter stall average price ($): 3.50
Category: Budget
```

**Sample 2**
```
Enter stall average price ($): 4.00
Category: Standard
```

**Sample 3**
```
Enter stall average price ($): 7.60
Category: Premium
```

---

## Guided Questions

**1.** How many `elif` branches do you need for 3 categories?

> _________________________________________________________________

**2.** Trace price = 4.00 through your chain step by step. Which branch runs?

> _________________________________________________________________

**3.** Why is `else` used for Premium instead of `elif price >= 7.00`?

> _________________________________________________________________

**4.** What is the problem with using three separate `if` statements here instead of `if`/`elif`/`else`?

> _________________________________________________________________

**5.** Complete the condition for each branch:

| Branch | Condition |
|--------|-----------|
| Budget | `if price _____ 4.00:` |
| Standard | `elif price _____ 7.00:` |
| Premium | `else:` |

---

## Common Mistakes

1. **Wrong boundary for Standard** — the condition is `price < 7.00`, not `price <= 7.00`. A price of exactly $7.00 belongs to Premium, not Standard.
2. **Using three separate `if` statements** — Python checks all three conditions every time. With `elif`, Python stops as soon as it finds a match — correct and efficient.
3. **Reversing the order** — if you check `price >= 7.00` first and then `price >= 4.00`, a $7.50 price would fall into Standard on the second check if you forget the first matched. Use ordered thresholds with `elif` to avoid this.
4. **Forgetting `float()`** — `input()` returns a string; comparing `"3.50" < 4.00` raises a `TypeError`.
