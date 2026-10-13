---
name: day-close
disable-model-invocation: true
description: Use at the end of a working day to close it out and pre-decide tomorrow. Reviews what actually happened, captures loose figures and commitments before they evaporate, proposes tomorrow's focus area, writes tomorrow's plan file and lays calendar blocks if a calendar tool is configured. Reads everything personal from references/tagesritual.md, written by /day-setup. Trigger on "close the day", "/day-close", "feierabend", "wrap up", "plan tomorrow". Pairs with /day-open.
---

## Step 0 — read the configuration

Read `references/tagesritual.md` before anything else. If it does not exist,
say exactly one line — *„Noch kein Tagesritual eingerichtet. Führe `/day-setup`
aus."* — and stop.

Everything personal lives in that file: who the user is, their areas and
priorities, the questions to ask in the evening, the tools, the tensions to
name, and what never enters the ritual. Below it is referenced as
`Konfig → <Überschrift>`. This skill itself names no person, area, currency or
tool; where an example is needed it is marked as an example and invented.

## What this skill does

Ends the working day with a decision instead of a fade-out. Five minutes. It is
the **producer** in a two-skill pair — it writes the plan that `/day-open` reads
back the next morning.

It exists to attack the pain named in `Konfig → Kopf` — typically: no daily
plan, reactive execution, no mapping of areas to time. The fix is a ritual, not
an automation. This skill is the ritual's container.

**Design constraint that governs everything below: people build good
instruments and then stop feeding them** (`Konfig → Kopf` names the user's own
version of this). So this skill stays short, never scolds, and never requires
yesterday to have gone well in order to run today. If it starts feeling like
homework, it is broken — say so and cut it down.

## What this skill is NOT

- Not a task manager. It holds *one day*. There is no backlog here.
- Not `/level-up`. That finds automations weekly. This runs the day.
- Not the author of the ritual. The user shapes the rhythm; this skill holds it.
  If they want a section changed, change it in `references/tagesritual.md` or
  the template — don't defend the template.

## Today's context

- **Date:** !`date +%Y-%m-%d`
- **Tomorrow:** !`date -v+1d +%Y-%m-%d`
- **Weekday tomorrow:** !`date -v+1d +%A`
- **Tomorrow 00:00 local:** !`date -v+1d +%Y-%m-%dT00:00:00$(date +%z | sed 's/\(..\)$/:\1/')`
- **Day after 00:00 local:** !`date -v+2d +%Y-%m-%dT00:00:00$(date +%z | sed 's/\(..\)$/:\1/')`

## Inputs to read

Read these **before** asking anything. Arriving with the context already loaded
is what keeps this to five minutes.

| Source | Why |
|---|---|
| Daily folder (`Konfig → Werkzeuge` → Tagesdatei) — most recent file | What was planned. Also: how many days since the last close. |
| `Konfig → Abends erfassen` → *Vorher lesen* | The priorities source, the areas, the calendar for tomorrow, mail only if something looks unresolved. Each in the order listed there. |

For the calendar: use the calendar tool from `Konfig → Werkzeuge`, if one is
configured, with the two local-midnight values injected above **verbatim**.
Never a UTC `…T00:00:00Z` timestamp: it shifts the window by the timezone
offset, drops early events and pulls in the tail of the previous day. No
calendar tool configured: skip the calendar, do not mention it.

Do not read the whole daily history. Last file plus a count is enough.

## Execution — four steps

### Step 1 — Look back (2 min)

Open today's daily file — written last night, and the file 4a will close — and
ask, plainly:

> *"Today's focus was **[X]**. What actually happened?"*

Then listen. Record the honest version, including nothing-happened. Do not
reframe a bad day as a learning opportunity — match the tone in
`Konfig → Kopf`: direct, findings not softened to be polite.

**If the last close was 2+ days ago,** state the gap in one neutral sentence
(*"Last close was Thursday — three days"*) and move on. One sentence. Not a
lecture. The habit dies faster from shame than from skipped days.

**If there is no daily file at all,** this is the first run. Skip straight to
Step 2 and say so.

### Step 2 — Capture the loose things (1 min)

This is the highest-value minute in the skill. Commitments made on a call or
in person exist only in memory until written down, and whatever
`Konfig → Abends erfassen` tracks in figures is tracked nowhere else.

Ask **exactly the questions listed in `Konfig → Abends erfassen` → *Die
Fragen***, in that order, in that wording, with the rules attached to each
question (what counts, when to stop asking, what to propose in Step 3). Do not
add questions; do not skip one because yesterday's answer was "none".

The answers split across **two** files in Step 4 — get the split right or the
capture is wasted:

- **Facts about today** — what happened, and every figure the configured
  questions capture — go into today's file under `## Evening review` (Step 4a).
- **Promises and open loops** are work for tomorrow. They go into tomorrow's
  file under `## Carried over` (Step 4b). A promise also gets written to the
  Evening review as a record that it was made.

If a commitment has a date attached, it becomes a calendar candidate in Step 4c.

**Always ask which area** anything money-shaped belongs to, unless it is
obvious — see the rules in `Konfig → Bereiche`. Separate books stay separate.
Do not be the thing that breaks that.

### Step 3 — Decide tomorrow (2 min)

**Propose, then let the user pick.** This was decided explicitly: the skill does
not own the area map.

Offer **two or three** candidate focuses for tomorrow, each one area, each with
a reason. Draw them from:

- the priorities in the source named in `Konfig → Bereiche`
- what has gone stale — which area has not appeared in the daily folder
  recently
- anything with a real date attached: `Konfig → Abends erfassen` →
  *Terminquellen* (the calendar, a promise from Step 2, dated carry-overs)

If the configured questions include a daily step of some kind, propose **one
concrete step for tomorrow** alongside the focus, as the question's rule says.

**The tensions in `Konfig → Spannungen` you must surface, not resolve.** If
tomorrow leans to one side of a named tension, say out loud what the other side
is losing. Do not present a plan that quietly implies everything fits. If the
user asks to automate something that came up today, check whether the process
exists yet — usually it doesn't.

Then the user picks. Close the step with **one sentence naming tomorrow's
focus** — that sentence is the point of the whole ritual.

### Step 4 — Write it down and block the time

Two files get touched every evening. Both writes always happen, even on a bad
day, even if Step 3 produced only "rest".

**4a. Close today — append the review to today's daily file.** Fill the
`## Evening review` section at the bottom of today's file from Steps 1 and 2:
what happened, the configured capture lines (`Konfig → Abends erfassen` →
*Zeilen in der Tagesdatei*, evening part, in that order), and what was promised
to whom. Write `none` rather than leaving a field blank — a blank is ambiguous
later, `none` is data.

If today's file does not exist (today was itself a cold start, or this is the
first ever run), create it from the template with just the Evening review
section filled. Do not reconstruct a plan that never existed.

**Never skip 4a.** What the evening questions capture exists in no other system
— if it is not written here it is gone.

**4b. Plan tomorrow — write tomorrow's daily file** from the template: focus
line, the configured plan lines (e.g. a daily step agreed in Step 3), blocks,
carried-over promises, fixed calendar events, trade-off accepted.

**4c. Propose calendar blocks — only if `Konfig → Werkzeuge` names a calendar
tool with write access.** Otherwise the plan lives in the daily file alone;
say nothing about calendars. Turn the focus into 1–3 real time blocks. Keep it
honest — two focused blocks beat a colour-coded day the user won't follow.

Title blocks `<Area> — <what>` using the short names from `Konfig → Bereiche`.
Example (invented, not a configured case): `Shop — autumn catalogue proof`.

Use the write command exactly as `Konfig → Werkzeuge` gives it, including its
timezone. Whether a dry-run is still required for that command is stated there
too; if the configuration says nothing, dry-run the first write and show the
result.

⚠️ **What never drops:** show the proposed blocks in chat and wait for the
user's yes before they are written. That is the real protection — not the
dry-run.

Treat early blocks as an experiment: if the user ignores them for a week, stop
writing them and say so rather than filling a calendar nobody reads.

## The daily file template

**Read `references/daily-template.md`** before writing either file in Step 4.
It holds the exact headings and is shared with `/day-open`, which writes the same
format on a cold start. Do not keep a second copy of it here — one template, one
place, so the two skills cannot drift apart. The lines the template marks as
configurable come from `Konfig → Abends erfassen` → *Zeilen in der Tagesdatei*.

Each file ends up holding both the plan and its own honest post-mortem — which is
what makes drift visible over weeks.

## Closing line

End with the focus sentence and nothing else. No summary of the session, no
encouragement, no next-steps list. The user is finishing work, not starting it.

Never end a turn on a tool call when the text before it is for the user — the
text would not be shown. Write the files, then say the closing line.

## When to suggest logging a decision

If tonight produced a real decision — the kinds of decisions listed under
`Konfig → Werkzeuge` → *Entscheidungslog* — suggest an entry in the decision
log named there. Don't suggest it for ordinary daily choices; that dilutes the
log.
