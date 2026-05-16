# Q10 — Theme Park Ride Validator

**Topic:** Lists + Compound Conditions + elif Chain | **Week 3** | **Difficulty:** Medium-Hard (~6 marks)

---

## Skills Practiced

| Skill | Lecture |
|-------|---------|
| `not in` for list rejection | 3-1 |
| Flat `if`/`elif`/`else` chain for multi-stage validation | 3-2B |
| Compound `or` condition for out-of-range check | 3-2C |
| `.strip().upper()` for input normalisation | 2-1C |
| `int()` input cast | 2-1E |

---

## Problem

A theme park booking system validates ride requests before accepting them. A booking is
only valid when:

1. The ride code is in the list of operating rides
2. The rider's height is between **100 cm and 220 cm** (inclusive)

If the booking passes both checks, the system assigns a **category** based on height:

| Height | Category |
|--------|----------|
| Less than 140 cm | Junior |
| 140 cm to less than 180 cm | Standard |
| 180 cm and above | Thrill |

Use separate error messages for each type of invalid input.

```python
VALID_RIDES = ["R01", "R02", "R03", "R04", "R05", "R06", "R07", "R08"]
MIN_HEIGHT  = 100
MAX_HEIGHT  = 220
```

---

## Sample Runs

**Sample 1** — valid ride, valid height (Standard)
```
Enter ride code    : R03
Enter height (cm)  : 155
Ride booked — Category: Standard
```

**Sample 2** — ride code not in the list
```
Enter ride code    : R99
Enter height (cm)  : 155
Invalid ride code.
```

**Sample 3** — valid ride, height too low
```
Enter ride code    : R03
Enter height (cm)  : 95
Height out of range.
```

**Sample 4** — valid ride, valid height (Thrill)
```
Enter ride code    : R06
Enter height (cm)  : 185
Ride booked — Category: Thrill
```

---

## Guided Questions

**1.** List the two conditions that must BOTH be satisfied for a booking to be accepted.

> 1. _________________________________________________________________
> 2. _________________________________________________________________

**2.** Write the compound `or` condition that detects an out-of-range height:

> `elif height _____ MIN_HEIGHT _____ height _____ MAX_HEIGHT:`

**3.** Trace Sample 2 (R99, 155 cm): which branch runs and why?

> _________________________________________________________________

**4.** Trace Sample 3 (R03, 95 cm): which branch runs?

> _________________________________________________________________

**5.** Why should the ride code check come before the height check in the chain?

> _________________________________________________________________

---

## Common Mistakes

1. **Putting the height check before the ride code check** — if the ride is not operating, the rider's height is irrelevant. Check the ride first so your error messages are meaningful.
2. **Using `and` instead of `or` for the height range** — `height < 100 and height > 220` can never be True at the same time. Use `or`: out-of-range low *or* out-of-range high.
3. **Forgetting `.strip().upper()`** — `"r03"` is not in `VALID_RIDES` even though `"R03"` is. Normalise before checking.
4. **Using `float()` for height** — heights in this problem are whole numbers, so `int()` is the right choice. `int("155.5")` would raise a `ValueError`; `float()` would accept it but give a meaningless decimal height.
