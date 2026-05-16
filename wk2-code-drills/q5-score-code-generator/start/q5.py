# q5.py
# Programming Aptitude Test — Week 2 Practice Materials
# Description: Q5 — Score Code Generator (starter template)
# Week introduced: Week 2 Practice | Difficulty: Medium-Hard (~5 marks)

# ── Constants ────────────────────────────────────────────────────
ASCII_OFFSET = 65   # chr(65) = 'A' — the alphabet starts here
MODULO_BASE  = 4

# ── Step 1: Get input (keep as string for indexing) ───────────────
# HINT: Do NOT cast to int here — you need to index individual characters.
# TODO: Ask the user for a 4-digit score. Store it as score (a string).

# ── Step 2: Extract each digit as an integer ─────────────────────
# HINT: score[0] gives the first character as a string. int(score[0]) converts it.
# TODO: Extract d0, d1, d2, d3 from the score string.

# ── Step 3: Apply the code formula ───────────────────────────────
# Step A: sum of first digit (d0) and last digit (d3)
# TODO: Calculate step_a = d0 + d3

# Step B: second digit (d1) modulo MODULO_BASE
# HINT: The % operator gives the remainder. e.g. 6 % 4 = 2
# TODO: Calculate step_b = d1 % MODULO_BASE

# Step C: character code = step_a + step_b + ASCII_OFFSET
# TODO: Calculate char_code

# ── Step 4: Convert to character and display ─────────────────────
# HINT: chr(72) gives 'H'. Try it in the Python shell to see how it works.
# TODO: Convert char_code to a character using chr(). Store it as suffix.

# TODO: Print the result in the format: "Score code: {score}-{suffix}"
