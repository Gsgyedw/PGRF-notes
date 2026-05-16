# q8.py
# Programming Aptitude Test — Week 3 Practice Materials
# Description: Q8 — Student Canteen Discount (complete solution)
# Week introduced: Week 3 Practice | Difficulty: Medium (~5 marks)

# ── Constants ────────────────────────────────────────────────────
STUDENT_PREFIX = 'S'    # student IDs start with this letter
MIN_BILL       = 6.00   # minimum bill to qualify for discount
DISCOUNT_RATE  = 0.10   # 10% off

# ── Step 1: Get inputs ───────────────────────────────────────────
customer_id = input("Enter student ID    : ")
bill        = float(input("Enter bill amount ($): "))

# ── Step 2: Apply compound condition ─────────────────────────────
# Both must be True: ID starts with 'S' AND bill is at least $6.00
if customer_id[0] == STUDENT_PREFIX and bill >= MIN_BILL:
    discounted = bill * (1 - DISCOUNT_RATE)
    print("Discounted price: ${:.2f}".format(discounted))
else:
    print("Full price: ${:.2f}".format(bill))
