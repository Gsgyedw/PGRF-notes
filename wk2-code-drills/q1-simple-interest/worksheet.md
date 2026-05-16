# Q1 — Simple Interest Calculator

**Topic:** Input, Arithmetic, String Formatting | **Week 2** | **Difficulty:** Easy (~4 marks)

---

## Skills Practiced

| Skill | Lecture |
|-------|---------|
| `input()` with `float()` cast | 2-1E |
| Arithmetic: `*`, `/` | Week 1 |
| `.format()` with `:.2f` | 2-1B |

---

## Problem

A savings account earns **simple interest**. The formula is:

```
Interest = Principal × Rate × Time ÷ 100
Total    = Principal + Interest
```

Write a program that asks for the principal ($), annual rate (%), and time in years,
then displays the interest earned and total amount — both to 2 decimal places.

---

## Sample Runs

**Sample 1**
```
Enter principal ($)      : 1000
Enter annual rate (%)    : 5
Enter time (years)       : 3
Interest earned : $150.00
Total amount    : $1150.00
```

**Sample 2**
```
Enter principal ($)      : 2500
Enter annual rate (%)    : 3.5
Enter time (years)       : 2
Interest earned : $175.00
Total amount    : $2675.00
```

**Sample 3**
```
Enter principal ($)      : 500
Enter annual rate (%)    : 10
Enter time (years)       : 1.5
Interest earned : $75.00
Total amount    : $575.00
```

---

## Guided Questions

**1.** Why must you use `float()` here instead of `int()`?

> _________________________________________________________________

**2.** Complete the interest formula:

> `interest = _______ * _______ * _______ / _______`

**3.** Which Python format specifier gives exactly 2 decimal places?

> `:.______`

**4.** Fill in the blank to display the total with a `$` sign:

> `print("Total amount    : $______".format(total))`

**5.** What would happen if you forgot to divide by 100 in the formula?

> _________________________________________________________________

---

## Common Mistakes

1. **Not casting input** — `input()` returns a string. `"1000" * 5` does not work; use `float(input(...))`.
2. **Integer division** — if `principal` and `rate` are both `int`, `5 / 100` in Python 3 still gives `0.05` (true division). No issue here, but be careful if you ever use `//`.
3. **Wrong specifier** — `{:.2}` truncates to 2 significant figures, not 2 decimal places. You need `{:.2f}`.
4. **Forgetting `$` in the string** — the `$` goes inside the format string, not inside `{}`.
