"""Local vs. Global Variables & Scope
Module 1: Python Foundations

How to run: open a terminal in the folder that holds this file (and any
data file the code reads), then run:
    python3 Module1_Lesson4_local-vs-global-variables-scope_STUDENT.py

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.

Generated from deck_spec.yaml by generator/build_codealong_script.py;
edit the deck, not this file.
"""

# ===== 1. Local Scope, Live =====
# A generic example on purpose — not tied to any project scenario.
# Complete the TODOs below as you code along.
# This is supposed to raise NameError: run it, read the traceback, then comment
# out the raising line so the rest of the file runs.
print('----- 1. Local Scope, Live -----')
# TODO: define make_total() with a local variable total set
# to 100, returning it, then try printing total outside the
# function and watch what happens


# ===== 2. Reading a Global, Live =====
# A generic example on purpose — not tied to any project scenario.
# Complete the TODOs below as you code along.
print('----- 2. Reading a Global, Live -----')
# TODO: define tax_rate as a global, then write
# price_with_tax(price) that reads it without taking it as
# a parameter


# ===== 3. Refactor: Global to Parameter =====
# The same function from earlier, now with the dependency made explicit.
# Complete the TODOs below as you code along.
print('----- 3. Refactor: Global to Parameter -----')
# TODO: rewrite price_with_tax so tax_rate is a parameter
# instead of a global it secretly reads
tax_rate = 0.08
