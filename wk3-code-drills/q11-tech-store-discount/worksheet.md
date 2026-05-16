# Q11 — Tech Store Discount *(Aptitude Test Mirror)*

**Topic:** Combined Input + Compound Conditions + elif Chain | **Week 3** | **Difficulty:** Hard (~6 marks)

---

## Skills Practiced

| Skill | Lecture |
|-------|---------|
| Combined input parsing with `.split(",")` | 2-1C (aptitude test pattern) |
| `int()` and `float()` cast from a split result | 2-1E |
| Compound `and` in an elif condition | 3-2C |
| 3-branch `if`/`elif`/`else` | 3-2B |
| `.format()` with `:.2f` | 2-1B |

---

## About This Question

This question is a **direct mirror of the Programming Aptitude Test Q2 pattern**.
Every recent test set (2024 and 2025) presents a Q2 that asks you to:

1. Accept two values in **one `input()` string** separated by a symbol
2. Split the string and cast each part to the correct type
3. Apply a **3-branch if/elif/else** where the middle branch uses a compound condition

| Aptitude Test | Structure |
|---------------|-----------|
| 2025 Set A Q2 | `reputation;price` → 10% / 5% / full price |
| 2025 Set B Q2 | `strength,armour` → 3 damage formulas |

Completing this question gives you the full pattern before the test.

---

## Problem

A tech store gives discounts to members based on their **reward points** and
**purchase total**, entered as **one comma-separated string** (e.g. `150,350.00`).

| Condition | Discount |
|-----------|----------|
| Points ≥ 100 | 15% off |
| Points < 100 **and** purchase ≥ $200 | 8% off |
| All other cases | full price |

Write a program that:
1. Prompts for reward points and purchase total in one string
2. Splits the string to get `points` and `purchase`
3. Calculates and displays the amount to pay to **2 decimal places**

---

## The Split Pattern

To parse `"150,350.00"` into two separate values:

```python
raw      = input("Enter reward points and purchase total: ")
parts    = raw.split(",")          # parts = ["150", "350.00"]
points   = int(parts[0])           # first part  → integer
purchase = float(parts[1])         # second part → float
```

`split(",")` cuts the string at every comma and returns a list of sub-strings.
Index `[0]` is the left part, `[1]` is the right part.

---

## Sample Runs

**Sample 1** — points ≥ 100 → 15% discount
```
Enter reward points and purchase total: 150,350.00
Member discount applied (15%). Amount to pay: $297.50
```

**Sample 2** — points < 100 but purchase ≥ $200 → 8% discount
```
Enter reward points and purchase total: 60,250.00
Spend discount applied (8%). Amount to pay: $230.00
```

**Sample 3** — points < 100 and purchase < $200 → no discount
```
Enter reward points and purchase total: 30,150.00
No discount. Amount to pay: $150.00
```

---

## Guided Questions

**1.** What does `"150,350.00".split(",")` return?

> `[ _________, _________ ]`

**2.** After splitting, why must you cast `parts[0]` to `int` and `parts[1]` to `float`?

> _________________________________________________________________

**3.** Write the condition for the first branch (15% discount):

> `if points _____ 100:`

**4.** Write the compound condition for the 8% discount branch:

> `elif points _____ 100 and purchase _____ 200:`

**5.** Trace Sample 2 (`60,250.00`) through all three conditions:

| Branch | Condition | Result |
|--------|-----------|--------|
| `if` | `60 >= 100` | `___` |
| `elif` | `60 < 100 and 250.00 >= 200` | `___` |
| Discount applied? | | ___ |

---

## Common Mistakes

1. **Forgetting to split** — `int("150,350.00")` raises a `ValueError`. You must split the string first, then cast each part separately.
2. **Wrong separator** — `split(" ")` splits on a space, not a comma. Always match the separator to your input format.
3. **Casting in the wrong order** — `int(parts[1])` on `"350.00"` raises a `ValueError` because `"350.00"` is not a whole number. Use `float()` for the decimal value.
4. **Checking `points < 100` in the first branch** — the first `if` only needs `points >= 100`. In the `elif`, you do not need to re-state `points < 100` explicitly (it is already implied), but writing it makes the logic self-documenting.
