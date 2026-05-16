# Q3 — Canteen Spending Log Writer

**Topic:** File I/O (Append Mode) | **Week 2** | **Difficulty:** Medium (~5 marks)

---

## Skills Practiced

| Skill | Lecture |
|-------|---------|
| `open()` in append mode `"a"` | 2-2A |
| `.write()` and `.close()` | 2-2A |
| `.format()` with `:.2f` | 2-1B |
| `\n` newline in strings | 2-1A |

---

## Problem

You are building a personal spending tracker. Each time you eat at a canteen,
the program records the date, stall name, and amount spent in a file called
`spending_log.txt`.

Importantly, the program must **add to** the file each time it runs — it must
not erase previous entries.

Write a program that:
1. Asks for a date, stall name, and amount
2. Formats a log line as: `date | stall name | $amount`
3. Appends the line to `spending_log.txt`
4. Prints a confirmation

---

## Sample Runs

**Sample 1**
```
Enter date (DD/MM/YYYY)  : 25/04/2026
Enter stall name         : Uncle Bob's Noodles
Enter amount spent ($)   : 5.50
Entry saved to spending_log.txt.
Logged: 25/04/2026 | Uncle Bob's Noodles | $5.50
```

**Sample 2**
```
Enter date (DD/MM/YYYY)  : 26/04/2026
Enter stall name         : The Burger Shack
Enter amount spent ($)   : 8.90
Entry saved to spending_log.txt.
Logged: 26/04/2026 | The Burger Shack | $8.90
```

After running Sample 1 then Sample 2, `spending_log.txt` contains:
```
25/04/2026 | Uncle Bob's Noodles | $5.50
26/04/2026 | The Burger Shack | $8.90
```

---

## Guided Questions

**1.** What is the difference between file mode `"w"` and file mode `"a"`?

| Mode | What it does to an existing file |
|------|----------------------------------|
| `"w"` | |
| `"a"` | |

**2.** Why must you use `"a"` (not `"w"`) in this program?

> _________________________________________________________________

**3.** A log line must end with a newline. Which escape sequence adds one?

> _________________________________________________________________

**4.** Complete the format string for a log line:

> `log_line = "_____ | _____ | $_____.format(date, stall_name, amount)`

**5.** What happens if you forget `.close()` after writing?

> _________________________________________________________________

---

## Common Mistakes

1. **Using `"w"` mode** — this erases the file every time the program runs. All previous entries are lost.
2. **Forgetting `\n` at the end of the log line** — without it, the next entry gets appended to the same line in the file.
3. **Not closing the file** — data may not be flushed to disk, and other programs cannot read the file safely.
4. **Printing `log_line` directly** — it contains `\n` at the end, which prints a blank line. Use `.strip()` to remove it first.
5. **Casting `amount` to `int`** — `int("5.50")` raises a `ValueError`. Use `float()`.
