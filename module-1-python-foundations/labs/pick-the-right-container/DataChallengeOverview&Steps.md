# Data Challenge: Pick the Right Container

**GitBook quest:** [Quest 1.3-1.5: When the Crowd Grows · Pick the Right Container · Make It Survive](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-04-data-structures) (quest runs Days 6-8)

**Vocabulary from the reading** (use these words in your shareout): `Input Size`, `Big-O`, `Linear Scan`, `Lookup`, `Data Structure`, `Dictionary`, `Set`, `Serialization`

**Skills assessed:** Algorithmic Complexity (Big-O), Control Flow & Loops, AI Output Validation (see this lab's own `RUBRIC.md`)

**Estimated time:** ~60 minutes per day, across 3 days (15 min intro · 30 min group work · 15 min shareout, each day)

**Submitted once, at the end of Day 3.** The rubric grades all 3 days of this challenge together, so keep everything in one file and keep your earlier days' work visible.

## Scenario

A city transit agency hands you one service day out of its turnstile tap
log. The analytics team wants three things out of it:

- A count of the distinct cards that rode that day.
- The cards that rode more than once.
- A summary file the overnight job can pick up the next morning, without
  re-reading the raw log.

**What you already did, and what is different here.** Quest 1.1 and
Quest 1.2 asked whether your code gets the right answer. Every version
you write over these three days gets the right answer, so that question
is settled on line one and is not what you are graded on.

What is new is that your code now has to **report how much work it did**.
Every search and every loop you build here keeps a counter of the records
it looked at, and you compare those counters. This log is small. A real
service day is millions of taps, so the question is what happens to that
number when the log gets bigger.

You answer that by counting, not by timing. A stopwatch tells you about
one run on one laptop. A comparison count is the same on every machine in
the room, which is why it can go in a shareout and a timing cannot.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## What Each Day Is For

- **Day 1**: Count the comparisons a Linear Scan performs on 5, 10 and 20 rows and on the whole log. State the pattern in words before you run anything. Then say what the same code would cost on a log 10 times bigger. Say why a nested pass over the same rows answers that question very differently.
  - *Assessed today: Algorithmic Complexity (Big-O), Control Flow & Loops*
- **Day 2**: Build the same per-card tap count twice. Use two parallel lists the first time and a Dictionary the second time, and count the work each one does. Use a Set for the unique stations, then say why a list would have been the wrong container.
  - *Assessed today: Algorithmic Complexity (Big-O), Control Flow & Loops*
- **Day 3**: Serialize the summary to JSON and hit the error a Set causes. Fix it honestly. Then reload the file and prove the fast Dictionary lookup survived the round trip. Show that the Set did not.
  - *Assessed today: Control Flow & Loops, AI Output Validation*

## Ground Rules

**Do not use AI to write the code.** This challenge grades Algorithmic Complexity (Big-O) and Control Flow & Loops. If AI writes it, nothing has been measured.

**Use AI to understand, then check what it says.** The AI Toolkit below shows how, one skill at a time.

**New here:** Counting the work, not guessing at it. Every search here reports how many records it looked at. That turns a hunch into a number you can show.

**Swap driver and navigator every step.** Whoever is not typing asks the questions.

<details>
<summary>Using AI, and working as a pair - the standing rules</summary>

**AI is for understanding, not for answers.**

- Fair game: explain a concept, explain an error message, show you a *different* example than the one you need.
- Not fair game: pasting the task in and shipping what comes back. If you cannot explain a line without the screen, you do not have it.
- Always run it, and check it against a case you worked out by hand. AI will hand you code that runs and is wrong. That is the exact thing this module trains you to catch.

**How to challenge an explanation.** Ask for the source and go read it. Ask "what would make that wrong?" Ask the same question a second way in a new chat and see whether the answer holds. An answer that changes when you rephrase the question was never knowledge.

**If you do end up with AI-written code, interrogate it before you keep a line of it.**

- Ask it to explain the code line by line, then check that story against what the code does when you run it.
- Ask "what input breaks this?" Then feed it that input. An empty list, a missing field, a zero, a name that is not there.
- Hand it a case you worked out by hand and ask it to predict the output. If its prediction disagrees with your arithmetic, one of you is wrong and you need to know which.
- Ask for a second, different approach, then make it argue against the first one. Keep whichever you can defend yourself.

**Working as a pair.**

- The navigator owns the questions: "Why that comparison?" "What happens on the last row?"
- Say *why* before you agree. If neither of you can give a reason, test both ways.
- Go through AI output together, line by line, and say what each line does. Never one person pasting and the other nodding.
- Each of you submits your own copy, and has to be able to explain it alone.

- Before writing the Dictionary version, each person separately writes down a predicted comparison count for it. Then compare. The gap between your two guesses is more interesting than the answer, and it disappears the moment you run the code.
- Swap who types between the parallel-lists version and the Dictionary version. Whoever writes the slower one defends it in the shareout. Defending a version teaches you far more about it than watching somebody else type it.

</details>

> **AI techniques you have so far** (taught by Day 6)
>
> - **Verify against your own work** *(Module 0)*: Check every AI answer against a hand count, the data file, or a run of your own code.
> - **Make it explain** *(Module 0)*: Paste real output or a traceback and ask why. Make it predict before you run.
> - **Prompt to understand** *(Module 0)*: Ask about the idea on a made-up example, not your code, and ask for a source to read.
> - **How LLMs work** *(Day 5)*: It reads tokens, sees only its context window, stops at a training cutoff, and can answer differently each time.
> - **Task, Context, Evidence, Output (TCEO)** *(Day 5)*: Say the task, give the context, paste the evidence, and name the output you want.
> - **One-shot prompting** *(Day 5)*: Show one example of the answer shape you want, taken from a different problem.
>
> The tips below use only these.

## AI Toolkit

Each tip below pairs one skill this challenge grades with one way to use AI on it. Copy the prompt, then do the check. A prompt you never check is just a guess.

**Make it explain the output** (Algorithmic Complexity (Big-O)) · Technique: **Make it explain**, you learned this in Module 0

```text
I counted comparisons for two versions of the same tap count on one
day's log. Parallel lists: [your count]. Dictionary: [your count]. Rows in
the log: [your row count].

Explain why these two numbers grow differently as the log gets longer.
Use my numbers, not a general rule.
```

**Check:** Ask it to predict both counts for a log 10 times longer, then do that arithmetic yourself. Its pattern should match the one you wrote in step 2. If it does not, ask which of you is wrong, and check.

**Spell out the spec** (Algorithmic Complexity (Big-O)) · Technique: **Task, Context, Evidence, Output (TCEO)**, you learned this on Day 5

```text
Task: Check my rule for counting comparisons. Do not write code.

Context: I am learning Big-O. My scan walks a list of tap IDs from the
top and stops at the first match.

Evidence: Here is my counting rule, in my own words:
[paste your rule]

Output: Ask me 2 questions about anything my rule leaves unclear. Then
say what my rule would count for the best case, the worst case and the
not-found case on a list of 10 items.
```

**Check:** Answer its questions in a comment in your file. Then work the 10-item cases on paper and run your scan on `taps[:10]`. Your counter, your paper and its answer should all agree.

**Validate against your own work** (Control Flow & Loops) · Technique: **One-shot prompting**, you learned this on Day 5

```text
A scan walks a list from the top and stops at the first match. For each
case, tell me how many comparisons it makes. Answer in exactly this
shape:

Example: list A, B, C, find B | comparisons: 2 | found: yes

Now do these:
list K, L, M, N, find K
list K, L, M, N, find N
list K, L, M, N, find Z
```

**Check:** Work all three on paper before you read its answer. If its shape or its counts differ from yours, recount. Then check that your own scan counts the same way on a 4-item slice of `taps`.

**Validate against your own work** (AI Output Validation) · Technique: **How LLMs work**, you learned this on Day 5

```text
Is looking up a key in a Python dictionary O(1)? Give me your source.
Then tell me what would make that answer wrong.
```

**Check:** Ask the same question in a new chat, since a model can answer differently each time. Keep only what both answers and the source agree on. Then check your own `lookups` counter from step 4. Did the work grow with the rows, or stay at one per lookup?

**Prompt to understand** (AI Output Validation) · Technique: **Prompt to understand**, you learned this in Module 0

```text
Which Python types can JSON hold, and which can it not? Use a small
made-up dictionary as the example, not my code. Name the docs page that
lists the conversions.
```

**Check:** Before you read its answer, name the key in your own `summary` that broke in step 5. Then find the conversion table on the docs page and check that key's type against it.

## The Data

- **File:** `data/station_taps.csv` (CSV)
- **Where it comes from:** Created for this challenge.

**Before you write any code, open the file and look at it.** You will not be told what is in here. Finding out is the first part of the work. Answer these three:

1. What does one row represent?
2. Which fields hold numbers, and which hold text?
3. What already looks wrong, missing or inconsistent?

*Answer them at the top of `pick-the-right-container_STUDENT.py`, under THE DATA.*

A later LiveLab explains `open()` and file formats properly. Here you
are graded on cost and containers, not on parsing, so the loader is
handed to you. Paste it and move on.

```python
with open("data/station_taps.csv") as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]
```

`rows[0]` is the header line and `taps` is every line after it. What
they hold is what you open the file to find out. Two things to know:

- Every field comes out of that `split` as a string, whatever it looks
  like.
- A `FileNotFoundError` means you are running from the wrong folder,
  not that the file is missing.

## Your Objectives

## Day 1

- **Step 1: Count the Comparisons a Linear Scan Makes for Three Different Tap IDs**
  - *`T999` is not in the file, and that is deliberate.*
    1. **Predict all three counts in the `# Predictions` comments of this step, and say how you got each one.** Two you can derive from the ids. Tap ids are numbered in file order starting at `T001`, so a tap's row position is the number in its id. A scan that stops on a match has made exactly that many comparisons. `T999` has no position to read. Predict it from the rule instead: what makes a scan stop, and what happens when nothing ever does?
    2. **Start the `comparisons` accumulator** at nothing.
    3. **Write the scan.** Walk `records` one row at a time, add one to `comparisons` before each comparison, and stop the moment you have a match.
    4. **Return the count either way.** A scan that finds nothing still did the work, and the next step needs that number.
    5. **Run it, and compare all three counts** against your predictions.

  *Then say which of the three is the number you should plan around.*

  *Work in `pick-the-right-container_STUDENT.py` under Step 1: complete its TODOs.*

  <details>
  <summary>Stuck? Open this.</summary>

  Test two calls you can check without the file. `scan_for("T001", taps)` must return 1, because `T001` is the first row. `scan_for("T999", taps)` must equal `len(taps)`, because nothing let it stop early. If `T001` comes back the same as `T999`, your scan never stops on a match: look for a missing `return` inside the `if`. If `T999` comes back 0, your counter only moves on a match, so it is counting matches, not comparisons. Move it above the `if`.

  </details>

- **Step 2: Compare Scan Cost Against Nested-Pass Cost as the Row Count Grows**
  - *No skeleton for this step. The written predictions are the main deliverable, and the code checks them.*
    1. **Write every number down first, with the arithmetic beside it**, under `# Your answer:`. For the scan: the worst-case count at 5, 10 and 20 rows and on the whole log. For the pair loop: the count on the whole log. Then both again with the row count multiplied by 10.
    2. **Print the worst-case scan count at 5, 10 and 20 rows and on the whole log**, reusing your `scan_for`. Slicing `taps[:size]` gives you a shorter log.
    3. **Write a nested pass** that compares every tap against every tap, itself included, and counts the pairs. That shape is what you would need to catch two taps on the same card within a minute.
    4. **Print both counts for a log 10 times this size.** Use arithmetic, since there is no bigger file.
    5. **Say each pattern in one sentence**, without notation. One sentence for the scan, one for the pair loop.

  *Both shapes finish instantly here. A stopwatch cannot tell them apart, which is exactly the point.*

  *Work in `pick-the-right-container_STUDENT.py` under Step 2. Write your answer as `#` comments under its `# Your answer:` line.*

  <details>
  <summary>Stuck? Open this.</summary>

  Count a tiny pair loop by hand first. With 3 rows, list every `(a, b)` pair the two loops visit, then do the same with 4 rows. Compare each pair count with its row count and look for the multiplication. Then run your nested pass on `taps[:3]` and `taps[:4]` and check it matches your list.

  </details>

### Share Out: Day 1

**Last 15 minutes, back together as a class. Bring:**

- **Your three comparison counts**, and which one you would plan
  around. Say why the not-found count is the one that matters.
- **The pattern in words, not notation.** One for the scan, one
  for the nested pass.
- **What each number becomes at 10x the rows.** Say which of the
  two shapes you would be worried about.
- **Where your prediction was wrong**, if it was. A wrong
  prediction you can explain beats a right one you guessed.

Be ready to answer **"why did you do it that way?"**

## Day 2

- **Step 3: Count Taps Per Card With Two Parallel Lists, and Count What It Costs**
  - *Two lists kept in step with each other by hand: `card_ids[3]` and `tap_counts[3]` have to describe the same card.*
    1. **Set up `card_ids`** - every distinct card, in the order you first meet it.
    2. **Set up `tap_counts`** - the count for `card_ids[i]`, held at that same index `i`.
    3. **Set up the `comparisons` accumulator**, starting at nothing.
    4. **Write one pass over `taps`.** For each row's card id, scan the card ids collected so far, moving `comparisons` on by one for every comparison you make.
    5. **On a match**, bump the count at that same index and stop scanning.
    6. **With no match**, append to BOTH lists so they stay the same length.
    7. **Run it and write the comparison count down.** The next step needs something to compare itself against.

  *The comparison count is the deliverable here, not the totals.*

  *Work in `pick-the-right-container_STUDENT.py` under Step 3: complete its TODOs.*

  <details>
  <summary>Stuck? Open this.</summary>

  Check the totals first. Count `C001`'s rows in the file by eye and compare with `tap_counts[card_ids.index("C001")]`. If the totals are right but your comparison count differs from another group's, check two things. Does your inner scan `break` on a match? Does it scan `card_ids`, or every earlier row of `taps`? Each choice changes the count, and either is defensible if you can say which you did.

  </details>

- **Step 4: Rebuild the Same Counts With a Dictionary and a Set, and Compare the Cost**
  - *Same question, different container: the card is the Key and the count is the Value. No loop skeletons this time.*
    1. **Predict your lookup count from the rule, not the file.** A Dictionary is handed a Key and goes straight to it, so ask whether where a card sits in the file changes anything. Write one number and the one-sentence rule in the comment at the top.
    2. **Build `taps_by_card`** with the card id as the Key and the tap count as the Value, one Lookup per row.
    3. **Count those Lookups in `lookups`**, starting at nothing.
    4. **Build `stations`** as the distinct stations. Uniqueness is the container's job here, so there should be no `if not in` test anywhere in it.
    5. **Count into `repeat_riders`** how many cards have a count above 1.
    6. **Run it, then put your lookup count next to your parallel-lists comparison count.**
    7. **Under `# Your answer:`, type 2-3 bullets.** Finish "As the Input Size grows..." for each version, and say what a list would have cost you for `stations`.

  *Work in `pick-the-right-container_STUDENT.py` under Step 4: complete its TODOs. Write your answer as `#` comments under its `# Your answer:` line.*

  <details>
  <summary>Stuck? Open this.</summary>

  Hand-check two values before you trust the rest. Count `C001`'s rows in the file by eye and compare with `taps_by_card["C001"]`. Then list the station names in the file's third column and compare with `len(stations)`. If `stations.add(row)` raises `TypeError: unhashable type: 'list'`, you handed the Set the whole row instead of one field. If `lookups` is not your prediction, print it next to `len(taps)`.

  </details>

### Share Out: Day 2

**Last 15 minutes, back together as a class. Bring:**

- **Both comparison counts.** Parallel lists, and Dictionary. If
  yours do not match another group's, say so and find where the
  two loops diverge - that is the interesting case, not the
  embarrassing one.
- **Your argument for one container over the other.** Both
  printed the same cards and neither felt slow, so the counts do
  not settle it alone. Start with "as the Input Size grows..."
- **What the Set did for you** that a list would not have, and
  what the list version would have cost.
- **What building the dictionary cost** before a single lookup
  happened. Say when that build stops being worth it.

Be ready to answer **"why did you do it that way?"**

## Day 3

- **Step 5: Serialize the Summary to JSON and Read the TypeError a Set Causes** *(expect this to raise `TypeError`. That is the point, not a bug.)*
  - *This step is supposed to fail.*
    1. Fill in the four `None` values in `summary`: the row count, the distinct-card count, the stations container exactly as you built it (do not convert it to anything else yet), and the per-card counts.
    2. Run it, and read the error message before you change a single character.
    3. Write down which of the five keys caused the error, and why, in your own words.
    4. Note whether the `about to serialize` line printed before the error. That tells you when the break happened.

  *Do not fix it here. The deliverable is the real message plus your own explanation of it.*

  *Work in `pick-the-right-container_STUDENT.py` under Step 5: complete its TODOs. Write your answer as `#` comments under its `# Your answer:` line.*

  **Try with AI:** *Prompt to understand, you learned this in Module 0.* Ask AI which Python types JSON can hold, then find the conversion table on the `json` docs page yourself.

  <details>
  <summary>Stuck? Open this.</summary>

  The error message names a type. Add `for key in summary: print(key, type(summary[key]))` above the `json.dumps` line, run it again, and find the one value whose type matches the message.

  </details>

- **Step 6: Write the Summary to Disk, Reload It, and Check Which Types Survived**
  - *This writes a real file into `data/`.*
    1. **Change the `stations` value** in `summary` into a form JSON actually has. Do not remove the key, because the agency asked for it.
    2. **Write `summary` to `data/tap_summary.json`** with `json.dump()`, then read it back into `reloaded` with `json.load()`. That is two `with open(...)` blocks, one writing and one reading.
    3. **Open `data/tap_summary.json` in your editor** and read it. It is plain text, so you can check it by eye.
    4. **Run the five prints.** Compare each container's type with the one you built on Day 2.

  *Then answer the agency: can the overnight job get one card's count from this file without re-reading the raw log? One container survived the round trip and one did not.*

  *Work in `pick-the-right-container_STUDENT.py` under Step 6: complete its TODOs.*

  <details>
  <summary>Stuck? Open this.</summary>

  Compare against what you built on Day 2, not against what you just wrote. Print `type(stations)` next to `type(reloaded["stations"])`, and `type(taps_by_card)` next to `type(reloaded["taps_by_card"])`. Then run `reloaded["stations"].append("Union Sq")` and print the length. Would your Day 2 `stations` have let that happen?

  </details>

### Share Out: Day 3

**Last 15 minutes, back together as a class. Bring:**

- **The error exactly as you first saw it**, plus your own
  one-sentence account of which key caused it. Written before you
  looked anything up.
- **What you did about it, and what that cost.** Did anything
  else in the summary quietly change on the way back out of the
  file?
- **How you proved the export worked.** Reloading and comparing,
  or trusting it?
- **If you used AI on the error:** what it said, whether it gave
  a source, and whether you could have explained the message
  without it.
- **One thing you would do differently.** A wrong prediction, a
  container you would pick differently, or a step where you
  guessed right and still cannot say why.

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `pick-the-right-container_STUDENT.py` (you may rename it `pick-the-right-container.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
