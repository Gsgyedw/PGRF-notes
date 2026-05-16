# q4.py
# Programming Aptitude Test — Week 2 Practice Materials
# Description: Q4 — Restaurant Bill Splitter (complete solution)
# Week introduced: Week 2 Practice | Difficulty: Easy-Medium (~4 marks)

# ── Step 1: Get inputs ───────────────────────────────────────────
total_bill = float(input("Enter total bill ($)    : "))
num_people = int(input("Enter number of people  : "))
tip_pct    = float(input("Enter tip percentage    : "))

# ── Step 2: Calculate ────────────────────────────────────────────
tip_amount  = total_bill * tip_pct / 100
grand_total = total_bill + tip_amount
per_person  = grand_total / num_people

# ── Step 3: Display ──────────────────────────────────────────────
print("Tip amount  : ${:.2f}".format(tip_amount))
print("Grand total : ${:.2f}".format(grand_total))
print("Per person  : ${:.2f}".format(per_person))
