# Q2 — Username Generator

**Topic:** String Indexing & Manipulation | **Week 2** | **Difficulty:** Easy-Medium (~5 marks)

---

## Skills Practiced

| Skill | Lecture |
|-------|---------|
| String indexing: `[0]`, `[-1]`, `[-2]` | 2-1C |
| `.lower()` on individual characters | 2-1C |
| String concatenation with `+` | 2-1A |
| `input()` with `.strip()` | 2-1E |

---

## Problem

A system auto-generates usernames using this rule:

```
Username = first 3 letters of first name (lowercase)
         + last 2 letters of last name (lowercase)
         + last 2 digits of birth year
```

For example: **Alice Tan, born 2003** → `ali` + `an` + `03` → **`alian03`**

Write a program that asks for a first name, last name, and birth year,
then prints the generated username.

**Assume:** First name has at least 3 characters. Last name has at least 2 characters.

---

## Sample Runs

**Sample 1**
```
Enter first name : Alice
Enter last name  : Tan
Enter birth year : 2003
Generated username : alian03
```

**Sample 2**
```
Enter first name : Bob
Enter last name  : Lim
Enter birth year : 1999
Generated username : bobim99
```

**Sample 3**
```
Enter first name : Charlie
Enter last name  : Wong
Enter birth year : 2001
Generated username : chang01
```

---

## Guided Questions

**1.** What index gives you the first character of a string?

> _________________________________________________________________

**2.** What index gives you the **last** character of a string without knowing its length?

> _________________________________________________________________

**3.** Write the expression for the first character of `first_name`, lowercased:

> `_______________________________`

**4.** Write the expression for the last 2 characters of `last_name`, lowercased:

> `part2 = _____________ + _____________`

**5.** Why do we use `.lower()` on name characters but not on `birth_year` characters?

> _________________________________________________________________

**6.** Trace through Sample 3 manually. What is `part1`? `part2`? `part3`?

| Part | Characters extracted | Value |
|------|---------------------|-------|
| part1 | first 3 of "Charlie" | `___` |
| part2 | last 2 of "Wong" | `___` |
| part3 | last 2 of "2001" | `___` |

---

## Common Mistakes

1. **Trying to use a slice like `[0:3]`** — indexing individual characters (`[0]`, `[1]`, `[2]`) is what you know at Week 2. Either approach produces the same result here.
2. **Forgetting `.lower()`** — `"Alice"[0]` gives `'A'`, not `'a'`. The rule says lowercase.
3. **Casting `birth_year` to `int`** — if you `int(birth_year)`, you can no longer index it. Keep it as a string.
4. **Using negative index on birth_year** — `birth_year[-2]` and `birth_year[-1]` work for any 4-digit year. Safe to use.
