# q1.py
# Programming Aptitude Test — Week 2 Practice Materials
# Description: Q1 — Simple Interest Calculator (complete solution)
# Week introduced: Week 2 Practice | Difficulty: Easy (~4 marks)

# ── Step 1: Get inputs ───────────────────────────────────────────
principal = float(input("Enter principal ($)      : "))
rate      = float(input("Enter annual rate (%)    : "))
years     = float(input("Enter time (years)       : "))

# ── Step 2: Calculate simple interest ───────────────────────────
# Formula: Interest = P × r × t ÷ 100
interest = principal * rate * years / 100
total    = principal + interest

# ── Step 3: Display ──────────────────────────────────────────────
print("Interest earned : ${:.2f}".format(interest))
print("Total amount    : ${:.2f}".format(total))
