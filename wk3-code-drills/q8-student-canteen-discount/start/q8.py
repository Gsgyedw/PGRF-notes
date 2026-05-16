# q8.py
# Programming Aptitude Test — Week 3 Practice Materials
# Description: Q8 — Student Canteen Discount (starter template)
# Week introduced: Week 3 Practice | Difficulty: Medium (~5 marks)

# ── Constants ────────────────────────────────────────────────────
STUDENT_PREFIX = 'S'    # student IDs start with this letter
MIN_BILL       = 6.00   # minimum bill to qualify for discount
DISCOUNT_RATE  = 0.10   # 10% off

# ── Step 1: Get inputs ───────────────────────────────────────────
# HINT: Keep customer_id as a string — you will index it with [0].
# TODO: Ask for the customer's ID. Store it as customer_id.

# HINT: Use float() so decimal bill amounts like 8.50 are accepted.
# TODO: Ask for the bill total. Store it as bill.

# ── Step 2: Apply compound condition ─────────────────────────────
# HINT: Use customer_id[0] == STUDENT_PREFIX to check the first character.
# HINT: Use `and` to require BOTH conditions to be True at once.
# TODO: Write the compound if condition (first character check AND bill check).

    # TODO: Calculate discounted = bill * (1 - DISCOUNT_RATE).
    # TODO: Print "Discounted price: $X.XX" formatted to 2 decimal places.

# TODO: Write the else branch for full price.

    # TODO: Print "Full price: $X.XX" formatted to 2 decimal places.
