# q10.py
# Programming Aptitude Test — Week 3 Practice Materials
# Description: Q10 — Theme Park Ride Validator (complete solution)
# Week introduced: Week 3 Practice | Difficulty: Medium-Hard (~6 marks)

# ── Constants ────────────────────────────────────────────────────
VALID_RIDES  = ["R01", "R02", "R03", "R04", "R05", "R06", "R07", "R08"]
MIN_HEIGHT   = 100
MAX_HEIGHT   = 220
JUNIOR_MAX   = 140    # below this → Junior
STANDARD_MAX = 180    # below this → Standard; at or above → Thrill

# ── Step 1: Get inputs ───────────────────────────────────────────
ride_code = input("Enter ride code    : ").strip().upper()
height    = int(input("Enter height (cm)  : "))

# ── Step 2: Validate ride code ───────────────────────────────────
# Check ride first — invalid ride is an immediate reject
if ride_code not in VALID_RIDES:
    print("Invalid ride code.")

# ── Step 3: Validate height range ────────────────────────────────
# `or` catches both ends: too short OR too tall
elif height < MIN_HEIGHT or height > MAX_HEIGHT:
    print("Height out of range.")

# ── Step 4: Classify by height category ──────────────────────────
# Reaching here means ride and height are both valid
elif height < JUNIOR_MAX:
    print("Ride booked — Category: Junior")
elif height < STANDARD_MAX:
    print("Ride booked — Category: Standard")
else:
    print("Ride booked — Category: Thrill")
