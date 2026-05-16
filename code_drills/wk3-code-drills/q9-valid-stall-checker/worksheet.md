# Q9 — Valid Stall Checker

**Topic:** List + `in` Operator | **Week 3** | **Difficulty:** Medium (~5 marks)

---

## Skills Practiced

| Skill | Lecture |
|-------|---------|
| List literal with multiple items | 3-1 |
| `in` operator for list membership | 3-1 |
| `.strip().upper()` for input normalisation | 2-1C |
| `if` / `else` | 3-2A |

---

## Problem

FoodClub OS keeps a list of **registered stall IDs**. Before accepting an order,
the system checks whether the stall ID entered by the customer is in the official list.

The registered stalls are:

```python
VALID_STALLS = ["S01", "S02", "S03", "S04", "S05",
                "S06", "S07", "S08", "S09", "S10", "S11"]
```

Write a program that:
1. Asks for a stall ID
2. Converts it to **uppercase** so that `s05` matches `S05`
3. Checks if it is in `VALID_STALLS`
4. Prints a found or not-found message using the normalised ID

---

## Sample Runs

**Sample 1** — valid ID entered in lowercase
```
Enter stall ID: s05
S05 is registered.
```

**Sample 2** — valid ID entered in uppercase
```
Enter stall ID: S08
S08 is registered.
```

**Sample 3** — stall ID not in the list
```
Enter stall ID: S99
S99 is not a valid stall ID.
```

---

## Guided Questions

**1.** What Python keyword checks if an item exists inside a list?

> `_____`

**2.** Write the condition to check if `stall_id` is in `VALID_STALLS`:

> `if stall_id _____ VALID_STALLS:`

**3.** Why must you call `.upper()` on the input before checking?

> _________________________________________________________________

**4.** What does `"S05" not in VALID_STALLS` evaluate to? What does `"S99" not in VALID_STALLS` evaluate to?

> _________________________________________________________________

**5.** After running the program, what does `VALID_STALLS` look like — has it changed?

> _________________________________________________________________

---

## Common Mistakes

1. **Checking `stall_id == VALID_STALLS`** — this compares the ID to the whole list object, not to items inside it. The result is always `False`. Use `in` for membership testing.
2. **Forgetting `.upper()`** — `"s05" in VALID_STALLS` is `False` because list membership is case-sensitive. Always normalise before checking.
3. **Using `.strip()` but not `.upper()`** — `.strip()` removes spaces but does not change letter case. Chain both: `.strip().upper()`.
4. **Thinking `in` changes the list** — `in` only *tests* membership. It does not add, remove, or modify any element.
