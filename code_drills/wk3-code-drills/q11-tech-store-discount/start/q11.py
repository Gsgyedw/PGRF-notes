# q11.py
# Programming Aptitude Test — Week 3 Practice Materials
# Description: Q11 — Tech Store Discount — Aptitude Test Mirror (starter template)
# Week introduced: Week 3 Practice | Difficulty: Hard (~6 marks)

# ── Constants ────────────────────────────────────────────────────
MEMBER_MIN       = 100     # points threshold for member discount
SPEND_MIN        = 200.00  # minimum purchase for spend discount
MEMBER_DISCOUNT  = 0.15    # 15% off
SPEND_DISCOUNT   = 0.08    # 8% off

# ── Step 1: Get combined input ───────────────────────────────────
# HINT: The input is ONE string like "150,350.00" — split it at the comma.
# TODO: Ask for reward points and purchase total in one input. Store it as raw.

# ── Step 2: Parse the two values ─────────────────────────────────
# HINT: raw.split(",") returns a list: ["150", "350.00"]
# TODO: Call raw.split(",") and store the result in parts.

# HINT: parts[0] is the points string (integer), parts[1] is the purchase string (float).
# TODO: Cast parts[0] to int and store as points.
# TODO: Cast parts[1] to float and store as purchase.

# ── Step 3: Apply discount logic ─────────────────────────────────
# HINT: Check the higher-value discount first (member points).
# TODO: Write the if branch — points >= MEMBER_MIN.

    # TODO: Calculate amount = purchase * (1 - MEMBER_DISCOUNT).
    # TODO: Print "Member discount applied (15%). Amount to pay: $X.XX"

# HINT: The elif needs a compound `and` — both conditions must be True.
# TODO: Write the elif branch — points < MEMBER_MIN and purchase >= SPEND_MIN.

    # TODO: Calculate amount = purchase * (1 - SPEND_DISCOUNT).
    # TODO: Print "Spend discount applied (8%). Amount to pay: $X.XX"

# TODO: Write the else branch for no discount.

    # TODO: Print "No discount. Amount to pay: $X.XX"
