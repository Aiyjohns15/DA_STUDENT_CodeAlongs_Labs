#!/usr/bin/env python3
<<<<<<< HEAD
"""Day 1 code-along: Control Flow & Conditionals. Run: python3 <file>"""

# ===== 1. If/Elif/Else, Live =====
# Print "Too hot", "Too cold", or "Just right" based on temperature.
print('----- 1. If/Elif/Else, Live -----')
# TODO: set temperature to any number
# TODO: write the if/elif/else check yourself
=======
"""Control Flow & Conditionals
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson1_control-flow-conditionals_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson1_control-flow-conditionals_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson1_control-flow-conditionals_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. If/Elif/Else, Live =====
# Print "Too hot", "Too cold", or "Just right" based on the value of
# temperature.
print('----- 1. If/Elif/Else, Live -----')
# TODO: set temperature to any number, then write the
# if/elif/else check yourself before revealing the answer
temperature = 71
if temperature > 71:
    print("Too hot!")
elif temperature < 71:
    print("Mucho frio!")
else:
    print("Just right!")
# ===== 2. For Loop, Live =====
# Print the four scores, one per line, so the output is 88, 92, 75, then 100.
print('----- 2. For Loop, Live -----')
# TODO: write a for loop that prints every value in scores
scores = [88, 92, 75, 100]
for item in scores:
    print(item)


# ===== 3. range() Generates Numbers to Loop Over =====
<<<<<<< HEAD
# Count from 0 to 4 with range(). Notice it stops before 5.
print('----- 3. range() Generates Numbers to Loop Over -----')
# TODO: use range() to print the numbers 0 through 4

# PREDICT before you run: Change range(5) to range(3). What prints now?
# Your answer:
#


# ===== 4. While Loop, Live =====
# Count up from 0 and stop after 3, printing 0, 1, 2, 3.
# DISCUSS: Put these in order: A: run body. B: check again. C: first check.
# Your answer:
#
print('----- 4. While Loop, Live -----')
# TODO: write a while loop that prints 0, 1, 2, 3 (check the condition!)
count = 0

# PREDICT before you run: Make it count < 3, not count <= 3. How many print?
# Your answer:
#


# ===== 5. Loop and Conditional, Together =====
# Label each score: 90+ gets "great job", lower gets "keep practicing".
print('----- 5. Loop and Conditional, Together -----')
# TODO: loop over scores; print "great job" if a score is 90 or above
# TODO: otherwise print "keep practicing"
=======
# Count from 0 up to 4 with range(), one number per line. Notice it stops
# before 5.
print('----- 3. range() Generates Numbers to Loop Over -----')
# TODO: use range() to print the numbers 0 through 4

# PREDICT before you run: Change range(5) to range(3). What does the loop print
#                         now?
# Your answer:
#
#
for x in range(5):
    print(x)

# ===== 4. While Loop, Live =====
# Count up from 0 and stop after 3, so the output is 0, 1, 2, 3 on separate
# lines.
#
# DISCUSS: Before you write the While Loop, Live code, put these steps in the
#          order Python runs them. A: Run the loop body. B: Check the condition
#          again. C: Check the condition the first time.
# Your answer:
#
#
print('----- 4. While Loop, Live -----')
# TODO: write a while loop that prints 0, 1, 2, 3 -
# think carefully about the condition
count = 0

# PREDICT before you run: In the While Loop, Live code above, change count <= 3
#                         to count < 3. How many numbers print?
# Your answer:
#
#
count = 0

while count <=3:
    print(count)
    count = count + 1
# ===== 5. Loop and Conditional, Together =====
# Label each score: 90 or above gets "great job", and anything lower gets "keep
# practicing".
print('----- 5. Loop and Conditional, Together -----')
# TODO: loop over scores; for each one, print "great job"
# if it's 90 or above, otherwise print "keep practicing"
>>>>>>> abf7f7b (Module 1 Days 1-4: livelabs/ + data-challenges/, .py code-alongs, README)
scores = [88, 92, 75, 100]
for item in scores:
    if item >=90:
        print(item, " - Great job!")
    else:
        print(item, " - Keep practicing.")
