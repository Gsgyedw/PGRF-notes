# q9.py
# Programming Aptitude Test — Week 3 Practice Materials
# Description: Q9 — Valid Stall Checker (complete solution)
# Week introduced: Week 3 Practice | Difficulty: Medium (~5 marks)

# ── Constants ────────────────────────────────────────────────────
VALID_STALLS = ["S01", "S02", "S03", "S04", "S05",
                "S06", "S07", "S08", "S09", "S10", "S11"]

# ── Step 1: Get input ────────────────────────────────────────────
# .strip() removes accidental spaces; .upper() normalises case so s05 matches S05
stall_id = input("Enter stall ID: ").strip().upper()

# ── Step 2: Check membership ─────────────────────────────────────
if stall_id in VALID_STALLS:
    print("{} is registered.".format(stall_id))
else:
    print("{} is not a valid stall ID.".format(stall_id))
