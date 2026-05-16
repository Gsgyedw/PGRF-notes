# q7.py
# Programming Aptitude Test — Week 3 Practice Materials
# Description: Q7 — Stall Price Category (complete solution)
# Week introduced: Week 3 Practice | Difficulty: Easy-Medium (~5 marks)

# ── Constants ────────────────────────────────────────────────────
BUDGET_MAX   = 4.00    # prices strictly below this are Budget
STANDARD_MAX = 7.00    # prices strictly below this are Standard; at or above → Premium

# ── Step 1: Get input ────────────────────────────────────────────
price = float(input("Enter stall average price ($): "))

# ── Step 2: Classify using if/elif/else chain ─────────────────────
# Python checks conditions in order and stops at the first True branch.
if price < BUDGET_MAX:
    print("Category: Budget")
elif price < STANDARD_MAX:
    print("Category: Standard")
else:
    print("Category: Premium")
