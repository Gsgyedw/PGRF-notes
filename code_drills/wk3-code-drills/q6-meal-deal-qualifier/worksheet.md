# Q6 — Meal Deal Qualifier

**Topic:** Basic if/else | **Week 3** | **Difficulty:** Easy (~4 marks)

---

## Skills Practiced

| Skill | Lecture |
|-------|---------|
| `if` / `else` with a comparison | 3-2A |
| `>=` comparison operator | 3-2A |
| `float()` input cast | 2-1E |
| `.format()` with `:.2f` | 2-1B |

---

## Problem

A food court runs a **Meal Deal** promotion. A customer qualifies for the Meal Deal
if their total spend is **at least $5.00**.

Write a program that:
1. Asks for the customer's total spend
2. Prints whether they qualify for the Meal Deal
3. Shows the total spend in both cases (formatted to 2 decimal places)

---

## Sample Runs

**Sample 1**
```
Enter total spend ($): 6.50
You qualify for a Meal Deal! Total: $6.50
```

**Sample 2**
```
Enter total spend ($): 5.00
You qualify for a Meal Deal! Total: $5.00
```

**Sample 3**
```
Enter total spend ($): 3.80
Sorry, spend at least $5.00 for a Meal Deal. Total: $3.80
```

---

## Guided Questions

**1.** Which comparison operator means "greater than or equal to"?

> `_____`

**2.** Complete the condition:

> `if spend _____ 5.00:`

**3.** Does spend = 5.00 qualify or not? Trace through your condition to check.

> _________________________________________________________________

**4.** Why use `float()` instead of `int()` for the spend amount?

> _________________________________________________________________

**5.** Which Python format specifier gives exactly 2 decimal places?

> `:.______`

---

## Common Mistakes

1. **Using `>` instead of `>=`** — `> 5.00` fails for exactly $5.00. "At least" means `>=`.
2. **Forgetting the colon** — `if spend >= 5.00` without `:` causes a `SyntaxError`.
3. **Indentation error** — the print inside `if` must be indented by 4 spaces. An unindented print runs unconditionally regardless of the condition.
4. **Wrong cast** — spend values like `5.50` need `float()`. Using `int()` on `"5.50"` raises a `ValueError`.
