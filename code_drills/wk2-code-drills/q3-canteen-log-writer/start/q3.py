# q3.py
# Programming Aptitude Test — Week 2 Practice Materials
# Description: Q3 — Canteen Spending Log Writer (starter template)
# Week introduced: Week 2 Practice | Difficulty: Medium (~5 marks)

LOG_FILE = "spending_log.txt"

# ── Step 1: Get inputs ───────────────────────────────────────────
# TODO: Ask for the date in DD/MM/YYYY format. Store it as date.

# TODO: Ask for the stall name. Store it as stall_name.

# HINT: Amount is a decimal — use float() to cast it.
# TODO: Ask for the amount spent. Store it as amount.

# ── Step 2: Format the log line ──────────────────────────────────
# HINT: Each entry should look like: "25/04/2026 | Uncle Bob's Noodles | $5.50"
#       Use .format() with :.2f for the amount.
#       Add \n at the end so each entry goes on its own line.
# TODO: Build log_line using .format().

# ── Step 3: Append to file ───────────────────────────────────────
# HINT: Use "a" mode — it adds to the file without erasing it.
#       "w" mode would erase the file each time. Which do you want here?
# TODO: Open LOG_FILE in append mode.

# TODO: Write log_line to the file.

# TODO: Close the file.

# ── Step 4: Confirm to user ──────────────────────────────────────
# HINT: Use .strip() on log_line when printing so the \n doesn't appear.
# TODO: Print a confirmation message showing the filename and what was logged.
