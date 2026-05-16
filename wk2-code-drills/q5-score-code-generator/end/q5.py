# q5.py
# Programming Aptitude Test — Week 2 Practice Materials
# Description: Q5 — Score Code Generator (complete solution)
# Week introduced: Week 2 Practice | Difficulty: Medium-Hard (~5 marks)

# ── Constants ────────────────────────────────────────────────────
ASCII_OFFSET = 65   # chr(65) = 'A'
MODULO_BASE  = 4

# ── Step 1: Get input (keep as string for indexing) ───────────────
score = input("Enter 4-digit score: ")

# ── Step 2: Extract each digit as an integer ─────────────────────
d0 = int(score[0])
d1 = int(score[1])
d2 = int(score[2])
d3 = int(score[3])

# ── Step 3: Apply the code formula ───────────────────────────────
# Step A: sum of first and last digit
step_a = d0 + d3
# Step B: second digit modulo 4
step_b = d1 % MODULO_BASE
# Step C: add both steps plus ASCII offset to get a character code
char_code = step_a + step_b + ASCII_OFFSET

# ── Step 4: Convert to character and display ─────────────────────
suffix = chr(char_code)
print("Score code: {}-{}".format(score, suffix))
