# q6.py
# Programming Aptitude Test — Week 3 Practice Materials
# Description: Q6 — Meal Deal Qualifier (complete solution)
# Week introduced: Week 3 Practice | Difficulty: Easy (~4 marks)

# ── Constants ────────────────────────────────────────────────────
MEAL_DEAL_MIN = 5.00   # minimum spend to qualify for the Meal Deal

# ── Step 1: Get input ────────────────────────────────────────────
spend = float(input("Enter total spend ($): "))

# ── Step 2: Check qualification ──────────────────────────────────
# >= means "at least" — spend of exactly $5.00 still qualifies
if spend >= MEAL_DEAL_MIN:
    print("You qualify for a Meal Deal! Total: ${:.2f}".format(spend))
else:
    print("Sorry, spend at least $5.00 for a Meal Deal. Total: ${:.2f}".format(spend))
