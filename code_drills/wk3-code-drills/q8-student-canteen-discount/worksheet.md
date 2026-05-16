# Q8 — Student Canteen Discount

**Topic:** Compound `and` Condition | **Week 3** | **Difficulty:** Medium (~5 marks)

---

## Skills Practiced

| Skill | Lecture |
|-------|---------|
| Compound condition with `and` | 3-2C |
| String indexing `[0]` used in a condition | 2-1C |
| `float()` input, arithmetic (`*`) | 2-1E |
| `.format()` with `:.2f` | 2-1B |

---

## Problem

A school canteen gives a **10% discount** when **both** of these conditions are true:

1. The customer's ID starts with the letter **`'S'`** (student ID)
2. Their bill total is **at least $6.00**

If either condition fails, the customer pays **full price**.

Write a program that asks for the customer's ID and bill total, then displays either the
discounted price or the full price.

---

## Sample Runs

**Sample 1** — both conditions met
```
Enter student ID    : S12345
Enter bill amount ($): 8.50
Discounted price: $7.65
```

**Sample 2** — ID starts with 'S' but bill is too low
```
Enter student ID    : S12345
Enter bill amount ($): 4.00
Full price: $4.00
```

**Sample 3** — bill is high enough but ID does not start with 'S'
```
Enter student ID    : T99999
Enter bill amount ($): 9.00
Full price: $9.00
```

---

## Guided Questions

**1.** How do you check if a string's first character is `'S'`?

> `customer_id[_____] == '_____'`

**2.** Write the complete compound condition for the discount:

> `if _________________________ and _________________________:`

**3.** In Sample 2, which part of the compound condition is False?

> _________________________________________________________________

**4.** `and` requires both sides to be `True`. What happens to the whole expression if only one side is `True`?

> _________________________________________________________________

**5.** Calculate the discounted price manually for a $12.00 bill at 10% off:

> `discounted = 12.00 × (1 − _____) = _______`

---

## Common Mistakes

1. **Using `or` instead of `and`** — `or` grants the discount when just one condition is true (e.g. a non-student spending $8). The problem requires *both* conditions simultaneously.
2. **Comparing the whole ID** — `customer_id == 'S'` checks if the entire ID is the single letter S. Use `customer_id[0] == 'S'` to check just the first character.
3. **Wrong discount calculation** — 10% off means multiply by 0.90 (keep 90%). Subtracting 0.10 from the bill directly gives a $0.10 discount, not 10%.
4. **Forgetting `float()` for the bill** — `input()` returns a string; arithmetic on a string raises a `TypeError`.
