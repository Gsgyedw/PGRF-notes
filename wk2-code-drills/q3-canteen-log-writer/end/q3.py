# q3.py
# Programming Aptitude Test — Week 2 Practice Materials
# Description: Q3 — Canteen Spending Log Writer (complete solution)
# Week introduced: Week 2 Practice | Difficulty: Medium (~5 marks)

LOG_FILE = "spending_log.txt"

# ── Step 1: Get inputs ───────────────────────────────────────────
date       = input("Enter date (DD/MM/YYYY)  : ")
stall_name = input("Enter stall name         : ")
amount     = float(input("Enter amount spent ($)   : "))

# ── Step 2: Format the log line ──────────────────────────────────
# Each line: date | stall name | $amount
log_line = "{} | {} | ${:.2f}\n".format(date, stall_name, amount)

# ── Step 3: Append to file ───────────────────────────────────────
# "a" mode appends — it does NOT erase existing entries
log_file = open(LOG_FILE, "a")
log_file.write(log_line)
log_file.close()

# ── Step 4: Confirm to user ──────────────────────────────────────
print("Entry saved to {}.".format(LOG_FILE))
print("Logged: {}".format(log_line.strip()))
