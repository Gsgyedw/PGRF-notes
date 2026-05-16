# q10.py
# Programming Aptitude Test — Week 3 Practice Materials
# Description: Q10 — Theme Park Ride Validator (starter template)
# Week introduced: Week 3 Practice | Difficulty: Medium-Hard (~6 marks)

# ── Constants ────────────────────────────────────────────────────
VALID_RIDES  = ["R01", "R02", "R03", "R04", "R05", "R06", "R07", "R08"]
MIN_HEIGHT   = 100
MAX_HEIGHT   = 220
JUNIOR_MAX   = 140    # below this → Junior
STANDARD_MAX = 180    # below this → Standard; at or above → Thrill

# ── Step 1: Get inputs ───────────────────────────────────────────
# HINT: Normalise ride_code with .strip().upper() before checking the list.
# TODO: Ask for the ride code. Store it as ride_code (normalised).

# HINT: Heights are whole numbers — use int(), not float().
# TODO: Ask for the rider's height in cm. Store it as height.

# ── Step 2: Validate and classify ────────────────────────────────
# HINT: Check the ride code first. If invalid, reject immediately — no need to check height.
# TODO: Write the if branch — check if ride_code is NOT in VALID_RIDES.

    # TODO: Print "Invalid ride code."

# HINT: Use `or` — height is out of range if it is TOO LOW or TOO HIGH.
# TODO: Write the elif branch for an out-of-range height.

    # TODO: Print "Height out of range."

# HINT: Reaching here means ride and height are both valid. Now classify.
# TODO: Write the elif for Junior (height < JUNIOR_MAX).

    # TODO: Print "Ride booked — Category: Junior"

# TODO: Write the elif for Standard (height < STANDARD_MAX).

    # TODO: Print "Ride booked — Category: Standard"

# TODO: Write the else for Thrill.

    # TODO: Print "Ride booked — Category: Thrill"
