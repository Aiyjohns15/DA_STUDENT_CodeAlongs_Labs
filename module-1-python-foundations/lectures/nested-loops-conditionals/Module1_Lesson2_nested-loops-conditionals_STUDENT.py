"""Nested Loops & Conditionals
Module 1: Python Foundations

How to run: open a terminal in the folder that holds this file (and any
data file the code reads), then run:
    python3 Module1_Lesson2_nested-loops-conditionals_STUDENT.py

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.

Generated from deck_spec.yaml by generator/build_codealong_script.py;
edit the deck, not this file.
"""

# ===== 1. Nested Loop, Live =====
# A generic row/col example on purpose — not tied to any project scenario.
# Complete the TODOs below as you code along.
print('----- 1. Nested Loop, Live -----')
# TODO: write a nested loop that prints every (row, col)
# pair for row in range(2) and col in range(3)


# ===== 2. Nested Conditional, Live =====
# This exact two-level check — operation type, then value — is what the
# project's validate_line function needs.
# Complete the TODOs below as you code along.
print('----- 2. Nested Conditional, Live -----')
# TODO: check operation first; if it's "ADD", nest a second
# check confirming quantity is greater than 0
operation = "ADD"
quantity = -5


# ===== 3. Putting It Together: Loop + Nested Conditional =====
# A miniature version of the project's real validate_line function — a loop
# wrapping a nested conditional.
# Complete the TODOs below as you code along.
print('----- 3. Putting It Together: Loop + Nested Conditional -----')
# TODO: loop over transactions; for each line, split it into
# operation and amount, then nest the ADD/quantity check
# from the previous slide inside the loop
transactions = ["ADD 10", "REMOVE 3", "ADD -5"]
