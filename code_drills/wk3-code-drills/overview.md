# Week 3 Practice Questions

**Module:** PRGF — Programming Fundamentals
**Level:** Year 1 Polytechnic | **Target:** Week 3 (post-lecture practice)
**Questions:** 6 | **Estimated time:** ~30–45 min each

---

## Purpose

These questions reinforce the Week 3 lecture topics through short, standalone programs.
Each question maps directly to one or more Week 3 lecture sections and uses only
techniques available by the end of Week 3.

**Week 3 techniques added:** `if`, `elif`, `else`, lists `[]`, `append()`, `remove()`,
`len()`, `in` operator, compound conditions (`and`, `or`, `not`).

**Still not available:** `while`, `for`, `break`, `continue`, `def`, classes.

---

## Question Map

| Q | Title | Difficulty | Key Concepts | Lecture Sections |
|---|-------|------------|--------------|-----------------|
| [Q6](q6-meal-deal-qualifier/worksheet.md) | Meal Deal Qualifier | Easy | `if`/`else`, `>=` comparison | 3-2A |
| [Q7](q7-stall-price-category/worksheet.md) | Stall Price Category | Easy-Medium | `if`/`elif`/`else` chain | 3-2B |
| [Q8](q8-student-canteen-discount/worksheet.md) | Student Canteen Discount | Medium | Compound `and`, `float()`, `:.2f` | 3-2C, 2-1E |
| [Q9](q9-valid-stall-checker/worksheet.md) | Valid Stall Checker | Medium | List literal, `in` operator | 3-1, 3-2A |
| [Q10](q10-theme-park-ride-validator/worksheet.md) | Theme Park Ride Validator | Medium-Hard | List + compound `or` + elif chain | 3-1, 3-2B, 3-2C |
| [Q11](q11-tech-store-discount/worksheet.md) | Tech Store Discount | Hard | Combined input, `.split()`, compound `and` | 3-2B, 3-2C |

---

## Lecture Coverage

| Lecture | Topic | Covered by |
|---------|-------|-----------|
| 3-1 | Lists, indexing, `in` operator | Q9, Q10 |
| 3-2A | Basic `if`/`else`, colon, indentation | Q6, Q9 |
| 3-2B | `if`/`elif`/`else` chains | Q7, Q10, Q11 |
| 3-2C | Compound conditions: `and`, `or`, `not` | Q8, Q10, Q11 |

---

## Recommended Order

- **All topics (recommended):** Q6 → Q7 → Q9 → Q8 → Q10 → Q11
- **Selection structure focus:** Q6 → Q7 → Q8
- **List focus:** Q9 → Q10
- **Aptitude test preparation:** Q10 → Q11 (do these last — they combine everything)

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

Q11 (Tech Store Discount) is a **direct structural mirror** of the aptitude test Q2 pattern:

| Aptitude Test | Q11 Equivalent |
|---------------|---------------|
| 2025 Set A Q2: `reputation;price` → discount tiers | `points,purchase` → discount tiers |
| 2025 Set B Q2: `strength,armour` → damage branches | Same combined-input parsing pattern |

The compound-condition multi-branch structure (`if A → X`, `elif not A and B → Y`, `else → Z`)
appears in every set of the aptitude test. Q10 and Q11 together give you the full pattern.
