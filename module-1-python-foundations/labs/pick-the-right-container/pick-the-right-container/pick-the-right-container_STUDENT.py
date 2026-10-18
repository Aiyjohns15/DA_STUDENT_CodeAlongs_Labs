"""Data Challenge: Pick the Right Container
GitBook Quest 1.3-1.5: When the Crowd Grows · Pick the Right Container · Make It Survive

HOW TO RUN
    Open a terminal in the folder that holds data/ and run:
        python3 pick-the-right-container_STUDENT.py
    If this file sits one folder below data/, run it from the folder
    above instead:  python3 pick-the-right-container/pick-the-right-container_STUDENT.py

THE DATA      data/station_taps.csv

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (DataChallengeOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

AI TOOLKIT: prompts to try and how to check them are in
DataChallengeOverview&Steps.md.

SUBMIT
    Commit this file (you may rename it pick-the-right-container.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
    Submit once, at the end of Day 3. Keep every day's work in here.
"""

############################################################################
#  THE DATA: open data/station_taps.csv and look at it
#  before you write any code. The worksheet's "The Data" section
#  shows how to load it.
############################################################################

# 1. What does one row represent?
# Your answer:
#
#

# 2. Which fields hold numbers, and which hold text?
# Your answer:
#
#

# 3. What already looks wrong, missing or inconsistent?
# Your answer:
#
#

############################################################################
#  DAY 1
############################################################################

# ===== Step 1: Count the Comparisons a Linear Scan Makes for Three Different Tap IDs =====
# T999 is not in the file, and that is deliberate.
#
# 1. Predict all three counts in the # Predictions comments of this step,
#    and say how you got each one. Two you can derive from the ids. Tap ids
#    are numbered in file order starting at T001, so a tap's row position is
#    the number in its id. A scan that stops on a match has made exactly
#    that many comparisons. T999 has no position to read. Predict it from
#    the rule instead: what makes a scan stop, and what happens when nothing
#    ever does?
# 2. Start the comparisons accumulator at nothing.
# 3. Write the scan. Walk records one row at a time, add one to comparisons
#    before each comparison, and stop the moment you have a match.
# 4. Return the count either way. A scan that finds nothing still did the
#    work, and the next step needs that number.
# 5. Run it, and compare all three counts against your predictions.
#
# Then say which of the three is the number you should plan around.

with open("data/station_taps.csv") as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]

def scan_for(tap_id, records):
    comparisons = None  # TODO: the accumulator
    # TODO: the scan. Count each comparison, stop on a match.
    return comparisons

# Predictions (write all three before you run):
# T001:
# T040:
# T999:

print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# ===== Step 2: Compare Scan Cost Against Nested-Pass Cost as the Row Count Grows =====
# No skeleton for this step. The written predictions are the main
# deliverable, and the code checks them.
#
# 1. Write every number down first, with the arithmetic beside it, under the
#    "# Your answer:" line below. For the scan: the worst-case count at 5,
#    10 and 20 rows and on the whole log. For the pair loop: the count on
#    the whole log. Then both again with the row count multiplied by 10.
# 2. Print the worst-case scan count at 5, 10 and 20 rows and on the whole
#    log, reusing your scan_for. Slicing taps[:size] gives you a shorter
#    log.
# 3. Write a nested pass that compares every tap against every tap, itself
#    included, and counts the pairs. That shape is what you would need to
#    catch two taps on the same card within a minute.
# 4. Print both counts for a log 10 times this size. Use arithmetic, since
#    there is no bigger file.
# 5. Say each pattern in one sentence, without notation. One sentence for
#    the scan, one for the pair loop.
#
# Both shapes finish instantly here. A stopwatch cannot tell them apart,
# which is exactly the point.

# TODO: Compare Scan Cost Against Nested-Pass Cost as the Row Count Grows

# Your answer:
#
#

# ----- Share Out: Day 1 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Your three comparison counts, and which one you would plan around. Say
#   why the not-found count is the one that matters.
# - The pattern in words, not notation. One for the scan, one for the nested
#   pass.
# - What each number becomes at 10x the rows. Say which of the two shapes
#   you would be worried about.
# - Where your prediction was wrong, if it was. A wrong prediction you can
#   explain beats a right one you guessed.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#

############################################################################
#  DAY 2
############################################################################

# ===== Step 3: Count Taps Per Card With Two Parallel Lists, and Count What It Costs =====
# Two lists kept in step with each other by hand: card_ids[3] and
# tap_counts[3] have to describe the same card.
#
# 1. Set up card_ids - every distinct card, in the order you first meet it.
# 2. Set up tap_counts - the count for card_ids[i], held at that same index
#    i.
# 3. Set up the comparisons accumulator, starting at nothing.
# 4. Write one pass over taps. For each row's card id, scan the card ids
#    collected so far, moving comparisons on by one for every comparison you
#    make.
# 5. On a match, bump the count at that same index and stop scanning.
# 6. With no match, append to BOTH lists so they stay the same length.
# 7. Run it and write the comparison count down. The next step needs
#    something to compare itself against.
#
# The comparison count is the deliverable here, not the totals.

card_ids = None     # TODO: distinct cards, in first-seen order
tap_counts = None   # TODO: the count for card_ids[i], at index i
comparisons = None  # TODO: the accumulator

# TODO: one pass over `taps`, with an inner scan of card_ids.

busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")

# ===== Step 4: Rebuild the Same Counts With a Dictionary and a Set, and Compare the Cost =====
# Same question, different container: the card is the Key and the count is
# the Value. No loop skeletons this time.
#
# 1. Predict your lookup count from the rule, not the file. A Dictionary is
#    handed a Key and goes straight to it, so ask whether where a card sits
#    in the file changes anything. Write one number and the one-sentence
#    rule in the comment at the top.
# 2. Build taps_by_card with the card id as the Key and the tap count as the
#    Value, one Lookup per row.
# 3. Count those Lookups in lookups, starting at nothing.
# 4. Build stations as the distinct stations. Uniqueness is the container's
#    job here, so there should be no if not in test anywhere in it.
# 5. Count into repeat_riders how many cards have a count above 1.
# 6. Run it, then put your lookup count next to your parallel-lists
#    comparison count.
# 7. Under the "# Your answer:" line below, type 2-3 bullets. Finish "As the
#    Input Size grows..." for each version, and say what a list would have
#    cost you for stations.

# Prediction for `lookups`, and the rule it comes from:
#
taps_by_card = None   # TODO: card id Key, tap count Value
lookups = None        # TODO: the accumulator
stations = None       # TODO: the distinct stations
repeat_riders = None  # TODO: cards with more than one tap

print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Your answer:
#
#

# ----- Share Out: Day 2 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Both comparison counts. Parallel lists, and Dictionary. If yours do not
#   match another group's, say so and find where the two loops diverge -
#   that is the interesting case, not the embarrassing one.
# - Your argument for one container over the other. Both printed the same
#   cards and neither felt slow, so the counts do not settle it alone. Start
#   with "as the Input Size grows..."
# - What the Set did for you that a list would not have, and what the list
#   version would have cost.
# - What building the dictionary cost before a single lookup happened. Say
#   when that build stops being worth it.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#

############################################################################
#  DAY 3
############################################################################

# ===== Step 5: Serialize the Summary to JSON and Read the TypeError a Set Causes =====
# This step is supposed to fail.
#
# 1. Fill in the four None values in summary: the row count, the
#    distinct-card count, the stations container exactly as you built it (do
#    not convert it to anything else yet), and the per-card counts.
# 2. Run it, and read the error message before you change a single
#    character.
# 3. Write down which of the five keys caused the error, and why, in your
#    own words.
# 4. Note whether the about to serialize line printed before the error. That
#    tells you when the break happened.
#
# Do not fix it here. The deliverable is the real message plus your own
# explanation of it.
#
# This step is supposed to raise TypeError. Run it, read the traceback,
# answer below, then put a # in front of the line that raises so the steps
# after it can run.

import json

# Every value here came out of Day 2's work.
summary = {
    "service_day": "2026-03-02",
    "total_taps": None,      # TODO: how many rows the log holds
    "distinct_cards": None,  # TODO: how many distinct cards rode
    "stations": None,        # TODO: `stations`, exactly as built
    "taps_by_card": None,    # TODO: the per-card counts
}

print("about to serialize", len(summary), "keys")
text = json.dumps(summary, indent=2)
print(text)

# Your answer:
#
#

# ===== Step 6: Write the Summary to Disk, Reload It, and Check Which Types Survived =====
# This writes a real file into data/.
#
# 1. Change the stations value in summary into a form JSON actually has. Do
#    not remove the key, because the agency asked for it.
# 2. Write summary to data/tap_summary.json with json.dump(), then read it
#    back into reloaded with json.load(). That is two with open(...) blocks,
#    one writing and one reading.
# 3. Open data/tap_summary.json in your editor and read it. It is plain
#    text, so you can check it by eye.
# 4. Run the five prints. Compare each container's type with the one you
#    built on Day 2.
#
# Then answer the agency: can the overnight job get one card's count from
# this file without re-reading the raw log? One container survived the round
# trip and one did not.

summary["stations"] = None  # TODO: a form JSON actually has

# TODO: write `summary` to data/tap_summary.json, then read it back.
reloaded = None

print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# ----- Share Out: Day 3 -----
# Last 15 minutes, back together as a class. Bring:
#
# - The error exactly as you first saw it, plus your own one-sentence
#   account of which key caused it. Written before you looked anything up.
# - What you did about it, and what that cost. Did anything else in the
#   summary quietly change on the way back out of the file?
# - How you proved the export worked. Reloading and comparing, or trusting
#   it?
# - If you used AI on the error: what it said, whether it gave a source, and
#   whether you could have explained the message without it.
# - One thing you would do differently. A wrong prediction, a container you
#   would pick differently, or a step where you guessed right and still
#   cannot say why.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#
