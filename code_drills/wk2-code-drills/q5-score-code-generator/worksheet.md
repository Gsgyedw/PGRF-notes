# Q5 — Score Code Generator

**Topic:** String Indexing, Modulo, chr() | **Week 2** | **Difficulty:** Medium-Hard (~5 marks)

---

## Skills Practiced

| Skill | Lecture |
|-------|---------|
| String indexing on a number kept as string | 2-1C |
| `int()` cast of a single character | 2-1E |
| `%` modulo operator | 2-1D |
| `chr()` to convert a number to a character | 2-1E |
| `.format()` for output | 2-1B |

---

## Problem

A gaming app generates a code suffix from a player's 4-digit score using this formula:

```
Step A  =  digit[0]  +  digit[3]          (sum of first and last digit)
Step B  =  digit[1]  %  4                 (second digit, remainder when divided by 4)
Code    =  Step A  +  Step B  +  65       (add ASCII offset for 'A')
Suffix  =  chr(Code)                      (convert number to a letter)
```

The final output is: `Score code: {score}-{suffix}`

**Note:** `chr(65)` = `'A'`, `chr(66)` = `'B'`, …, `chr(90)` = `'Z'`

Write a program that takes a 4-digit score as input and prints the score code.

---

## Sample Runs

**Sample 1**
```
Enter 4-digit score: 1234
Score code: 1234-H
```

**Sample 2**
```
Enter 4-digit score: 5678
Score code: 5678-P
```

**Sample 3**
```
Enter 4-digit score: 9000
Score code: 9000-J
```

---

## Guided Questions

**1.** Why should you **not** cast the score to `int` immediately?

> _________________________________________________________________

**2.** How do you get the value of the first digit as an integer?

> `d0 = _______________________________`

**3.** Trace Sample 1 (`"1234"`) through the formula:

| Step | Expression | Value |
|------|------------|-------|
| d0 | `int("1234"[0])` | `___` |
| d1 | `int("1234"[1])` | `___` |
| d3 | `int("1234"[3])` | `___` |
| Step A | `d0 + d3` | `___` |
| Step B | `d1 % 4` | `___` |
| Code | `Step A + Step B + 65` | `___` |
| Suffix | `chr(Code)` | `___` |

**4.** What is `7 % 4`? What is `4 % 4`? What is `3 % 4`?

> _________________________________________________________________

**5.** In Sample 3 (`"9000"`), what is `d1 % 4`? Does it change the code?

> _________________________________________________________________

---

## Common Mistakes

1. **Casting score to int before indexing** — `int("1234")` gives `1234`, which you cannot index with `[0]`. Keep it as a string.
2. **Forgetting `int()` when extracting digits** — `score[0]` is the string `"1"`, not the number `1`. You need `int(score[0])` before doing arithmetic.
3. **Confusing `%` with division** — `d1 % 4` is the **remainder**, not the quotient. `6 % 4 = 2`, not `1.5`.
4. **Getting `ASCII_OFFSET` wrong** — `chr(65)` = `'A'`. If your answer is a lowercase letter or a symbol, your total is off by 32 or more — recheck the formula.
