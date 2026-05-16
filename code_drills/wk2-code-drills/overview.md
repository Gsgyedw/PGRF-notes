# Week 2 Practice Questions

**Module:** PRGF — Programming Fundamentals
**Level:** Year 1 Polytechnic | **Target:** Week 2 (post-lecture practice)
**Questions:** 5 | **Estimated time:** ~30 min each

---

## Purpose

These questions reinforce the Week 2 lecture topics through short, standalone programs.
Each question maps directly to one or more Week 2 lecture sections and uses only
techniques available by the end of Week 2.

**Week 2 techniques allowed:** `input()`, type casting (`float()`, `int()`, `str()`),
string indexing, `.lower()`, `.find()`, `.replace()`, `.format()`, `:.2f`,
arithmetic operators including `%` modulo, `chr()`, file I/O (`r`/`w`/`a` modes).

**Not yet available:** `if/elif/else`, loops, `def`, classes.

---

## Question Map

| Q | Title | Difficulty | Key Concepts | Lecture Sections |
|---|-------|------------|--------------|-----------------|
| [Q1](q1-simple-interest/worksheet.md) | Simple Interest | Easy | `float()`, arithmetic, `:.2f` | 2-1E, 2-1B |
| [Q2](q2-username-generator/worksheet.md) | Username Generator | Easy-Medium | String indexing, `.lower()`, `+` concat | 2-1C, 2-1A |
| [Q3](q3-canteen-log-writer/worksheet.md) | Canteen Log Writer | Medium | File I/O `"a"` mode, `\n`, `.format()` | 2-2A, 2-1B |
| [Q4](q4-bill-splitter/worksheet.md) | Bill Splitter | Easy-Medium | `float` vs `int`, arithmetic, `:.2f` | 2-1E, 2-1B |
| [Q5](q5-score-code-generator/worksheet.md) | Score Code Generator | Medium-Hard | String indexing, `%` modulo, `chr()` | 2-1C, 2-1D, 2-1E |

---

## Lecture Coverage

| Lecture | Topic | Covered by |
|---------|-------|-----------|
| 2-1A | Strings, escape sequences, `sep`/`end` | Q3 (`\n`), Q2 (concatenation) |
| 2-1B | String formatting, `.format()`, `:.2f` | Q1, Q3, Q4 |
| 2-1C | String manipulation, indexing, `.find()`, `.replace()` | Q2, Q5 |
| 2-1D | Operators: `%` modulo, assignment, `and`/`or` | Q5 |
| 2-1E | `input()`, type casting, `math` module | Q1, Q2, Q4, Q5 |
| 2-2A | File I/O: `r`/`w`/`a` modes | Q3 |

---

## Recommended Order

- **All topics (recommended):** Q1 → Q4 → Q2 → Q3 → Q5
- **Formatting focus:** Q1 → Q4
- **String manipulation focus:** Q2 → Q5
- **File I/O:** Q3 (standalone — do this after the 2-2A lecture)

---

## Three Levels Per Question

Each question folder contains three starting points — choose based on how much support you need:

| Folder | What's inside | When to use |
|--------|--------------|-------------|
| `start/` | Section dividers, `# HINT:`, `# TODO:` markers | First attempt — use if you're unsure where to begin |
| `challenge/` | Header comment and pre-given constants only | Once you've understood the pattern — no scaffolding |
| `end/` | Complete working solution | Check only after a genuine attempt |

## How to Use

1. Read `worksheet.md` — understand the problem and work through the guided questions on paper first.
2. Try `challenge/q{N}.py` first. If you get stuck, switch to `start/q{N}.py` for hints.
3. Run your solution against all sample runs in the worksheet. Output must match exactly.
4. Only open `end/q{N}.py` after a genuine attempt.

---

## Connection to Aptitude Test Style

Q5 (Score Code Generator) directly mirrors the style of aptitude test questions that
combine string indexing, modulo arithmetic, and `chr()` — the same pattern seen in
2024 Test 1 Set 2 Q2 (Inventory Suffix Generator) and practice question Q5 in
`../apptitude-test1/`.

Completing Q5 here is good preparation for those harder questions.
