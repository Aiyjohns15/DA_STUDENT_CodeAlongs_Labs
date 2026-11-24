#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    # TODO: assign `comparisons` to 0
    # TODO: loop over `members`; add 1 to `comparisons` for every row
    # TODO: inside the loop, return row, comparisons on a member_id match
    # TODO: after the loop, return None, comparisons
    comparisons = 0
    for member in members:
        comparisons += 1
        if row.member_id == member_id:
            return row, comparisons
    return None, comparisons    



row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1:
# 150 bc the code loops through 150 rows before getting member id 150


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
# TODO: open CHECKINS_FILE in a with block as `f`
# TODO: inside it, assign `swipes` to f.read().splitlines()
# TODO: assign `linear_total` and `not_members` to 0
# TODO: loop over `swipes`; call find_linear(members, member_id)
# TODO: print the ID, the name or "NOT A MEMBER", and the comparisons
# TODO: add each count to `linear_total`
# TODO: add 1 to `not_members` for every swipe with no row
with open(CHECKINS_FILE) as f:
    swipes = f.read().splitlines()
linear_total = 0
not_members = 0
for member_id in swipes:
    row, comparisons = find_linear(members, member_id)
    linear += comparisons
    if row is None:
        not_members +=1
        print(f"{member_id} | NOT A MEMBER | comparisons ; {comparisons}")
    else:
        print(f"{member_id} | {row['name']} | comparisons ; {comparisons}")

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)
print()
# Step 2, answer 1:
# The cost of the first 3 swipes are 4, 12, and 27. The sum is 43.
# The cost for a nonmember is 312
# Step 2, answer 2:
# The nonmember swipe costs the most bc the program had to run through the entire list


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off
# TODO: assign `members_by_id` to an empty dict and `build_steps` to 0
# TODO: loop over `members`; store each row under row["member_id"]
# TODO: add 1 to `build_steps` for every row
# TODO: write find_dict(members_by_id, member_id)
# TODO: make find_dict() return members_by_id.get(member_id), 1
members_by_id = {}
build_steps = 0

for row in members:
    members_by_id[row["member_id"]] = row 
    build_steps += 1

def find_dict(members_by_id, member_id):
    return members_by_id.get(member_id), 1
   
print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

# TODO: assign `linear_running` to 0 and `dict_running` to build_steps
# TODO: assign `pays_off_at` to None and `swipe_number` to 0
linear_running = 0
dict_running = build_steps
pays_off_at = None
swipe_number = 0

for member_id in swipes:
    swipe_number += 1
    # TODO: add 1 to `swipe_number`
    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)
    # TODO: add each search's count to its running total
    # TODO: print swipe_number, the ID and both running totals
    # TODO: the first time dict_running < linear_running, set `pays_off_at`
    linear_running = linear_count
    dict_running = dict_count
    print(swipe_number, member_id, linear_running, dict_running)
    if dict_running < linear_running:
        pays_off_at = swipe_number
print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1:
#At swipe 5 bc for M1313 the cost will be over 312
# Step 3, answer 2:
#A di ct fits the door's job bc you can look up the key value directly
# Step 3, answer 3:
# A plain list is a better choice on dat 1 bc member id M1004 appears very early on in the list and has a small linear cost


# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
# TODO: replace the text below with your AI's claim, word for word
ai_claim = "For a list of 312 members, a linear lookup can check up to 312 records to find a match, while a dictionary search can find a member by ID in approximately one lookup on average. 
Linear search gets slower as the list grows, whereas dictionary search is faster for repeated lookups,
although the dictionary requires an upfront cost to build."


# TODO: unpack find_linear() for swipes[0] into `_, front_count`
# TODO: unpack find_linear() for "M1313" into `_, absent_count`
# TODO: assign `ratio` to round(linear_running / dict_running, 1)
_, front_count = find_linear(members, swipe[0])
_, absent_count = find_linear(members, "M1313")
ratio = round(linear_running / dict_running, 1)
print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
    "| ratio:", ratio)

# TODO: replace the text below with your own verdict
verdict = "With O(n) the number of comparisons grows with the size of thelis so the amount of time that th searh takes grows as well." \
"An O(1) average case takes roughly the samse amount of time per look up regardless of the size of the list"
print("VERDICT:", verdict)

# Step 4, answer 1:
#
# Step 4, answer 2:
#
