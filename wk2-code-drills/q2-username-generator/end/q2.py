# q2.py
# Programming Aptitude Test — Week 2 Practice Materials
# Description: Q2 — Username Generator (complete solution)
# Week introduced: Week 2 Practice | Difficulty: Easy-Medium (~5 marks)

# ── Step 1: Get inputs ───────────────────────────────────────────
# Note: .strip() removes any accidental spaces the user may type
first_name = input("Enter first name : ").strip()
last_name  = input("Enter last name  : ").strip()
birth_year = input("Enter birth year : ").strip()

# ── Step 2: Extract parts ────────────────────────────────────────
# Rule: first 3 letters of first name + last 2 letters of last name + last 2 digits of year
# All lowercased
part1 = first_name[0].lower() + first_name[1].lower() + first_name[2].lower()
part2 = last_name[-2].lower() + last_name[-1].lower()
part3 = birth_year[-2] + birth_year[-1]

# ── Step 3: Build and display username ───────────────────────────
username = part1 + part2 + part3
print("Generated username : {}".format(username))
