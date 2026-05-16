# q11.py
# Programming Aptitude Test — Week 3 Practice Materials
# Description: Q11 — Tech Store Discount — Aptitude Test Mirror (complete solution)
# Week introduced: Week 3 Practice | Difficulty: Hard (~6 marks)

# ── Constants ────────────────────────────────────────────────────
MEMBER_MIN      = 100     # points threshold for 15% member discount
SPEND_MIN       = 200.00  # minimum purchase for 8% spend discount
MEMBER_DISCOUNT = 0.15
SPEND_DISCOUNT  = 0.08

# ── Step 1: Get combined input ───────────────────────────────────
raw = input("Enter reward points and purchase total: ")

# ── Step 2: Parse the two values ─────────────────────────────────
# split(",") returns ["150", "350.00"] — [0] is points, [1] is purchase
parts    = raw.split(",")
points   = int(parts[0])
purchase = float(parts[1])

# ── Step 3: Apply discount logic ─────────────────────────────────
if points >= MEMBER_MIN:
    amount = purchase * (1 - MEMBER_DISCOUNT)
    print("Member discount applied (15%). Amount to pay: ${:.2f}".format(amount))
elif points < MEMBER_MIN and purchase >= SPEND_MIN:
    amount = purchase * (1 - SPEND_DISCOUNT)
    print("Spend discount applied (8%). Amount to pay: ${:.2f}".format(amount))
else:
    print("No discount. Amount to pay: ${:.2f}".format(purchase))
