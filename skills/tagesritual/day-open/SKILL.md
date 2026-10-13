---
name: day-open
disable-model-invocation: true
description: Use first thing in a working day to read back the plan and start with a decision already made. Sixty seconds. Reads today's file from /day-close, checks the configured morning sources for anything that breaks it, confirms or adjusts. If no plan exists it degrades to a full cold brief instead of failing. Reads everything personal from references/tagesritual.md, written by /day-setup. Trigger on "open the day", "/day-open", "good morning", "what's today", "guten morgen". Pairs with /day-close.
---

## Step 0 — read the configuration

Read `references/tagesritual.md` before anything else. If it does not exist,
say exactly one line — *„Noch kein Tagesritual eingerichtet. Führe `/day-setup`
aus."* — and stop.

Everything personal lives in that file. Below it is referenced as
`Konfig → <Überschrift>`. This skill itself names no person, area or tool; where
an example is needed it is marked as an example and invented.

## What this skill does

Reads back a decision that was already made last night, so the day starts
decided instead of reactive. It is the **reader** in a two-skill pair —
`/day-close` produces the plan, this consumes it.

**Sixty seconds. Hard target.** This skill is deliberately the cheap half of the
pair. `/day-close` does the thinking; if this one grows into a second planning
session, the pair dies — two heavy daily rituals is one more than most track
records support (`Konfig → Kopf` says so for this user). Keep it short even when
there is a lot to say.

## The rule that matters most

**This skill must never fail because last night was skipped.** A missed evening
is the single most likely thing to break the chain, so the cold-start path
below is not an edge case — it is a first-class mode. Never open with a
variation of *"you didn't run /day-close"*. Just produce the brief.

## Today's context

- **Date:** !`date +%Y-%m-%d`
- **Weekday:** !`date +%A`
- **Today 00:00 local:** !`date +%Y-%m-%dT00:00:00$(date +%z | sed 's/\(..\)$/:\1/')`
- **Tomorrow 00:00 local:** !`date -v+1d +%Y-%m-%dT00:00:00$(date +%z | sed 's/\(..\)$/:\1/')`

## Inputs to read

Read everything before speaking. This is a report, not an interview.

| Source | Why |
|---|---|
| Today's daily file (`Konfig → Werkzeuge` → Tagesdatei) | The plan, if it exists. This is the primary input. |
| Every source in `Konfig → Morgens prüfen` | Read each with the command given there and report exactly what that row says to report — nothing more. Typical rows: today's calendar, overnight mail, logs of overnight background jobs. |

For a calendar row: use the two local-midnight values injected above
**verbatim**. Never a UTC `…T00:00:00Z` timestamp: it shifts the window by the
timezone offset, so an early event silently vanishes from the brief.

## Execution — two paths

### Path A — the plan exists (normal)

1. **Read the focus line back**, verbatim. One sentence. That is the headline.
   Then each configured plan line (`Konfig → Abends erfassen` → *Zeilen in der
   Tagesdatei*, plan part — e.g. a daily step), verbatim, on its own line. Read
   it, never grade it.
2. **List today's blocks and fixed events**, in time order. Nothing else.
3. **Report only what breaks the plan.** Overnight mail and calendar changes get
   one line *each*, and only if they collide with today's focus or carry a real
   deadline — the criteria are in `Konfig → Morgens prüfen`. Everything else
   waits — surfacing it here is exactly the reactive execution the ritual
   exists to stop.
4. **Ask one question:** *"Still the plan?"* If yes, stop. If no, adjust the
   focus line and the blocks in today's daily file, and note in the file that it
   was changed in the morning and why. That note is the drift signal
   `/day-close` reads later.

If a block needs moving and `Konfig → Werkzeuge` names a calendar tool with
write access, patch the existing event rather than deleting and recreating it,
with the command given there. Whether that command still needs a dry-run is
stated there too; if the configuration says nothing, dry-run the first patch
and show the result. No calendar tool: move the block in the daily file only.

### Path B — no plan file (cold start)

Say one neutral clause — *"No plan file for today, so here's a cold brief"* —
and then produce it. No comment on the missed evening.

Build the brief from what exists:

- Today's calendar (if a calendar source is configured)
- Anything unresolved in the most recent daily file
- The priorities source named in `Konfig → Bereiche`
- Which area has gone longest without appearing in the daily folder

Then propose **two candidate focuses**, one sentence each, and let the user
pick. Same rule as `/day-close`: propose, don't assign. If the configured plan
lines include a daily step, propose one with the focus candidates.

Surface the tensions in `Konfig → Spannungen` if they apply. One line each, not
a paragraph.

Once the user picks, write today's daily file — **read
`references/daily-template.md`** for the exact headings — so the chain is intact
from today onward. That is the recovery: a cold start ends with the same artifact
a normal night would have produced.

Leave the `## Evening review` section empty. Tonight's `/day-close` fills it.
Calendar blocks are never created here, so a cold-start plan lives in the daily
file alone; say so in the file's opening note.

## Mail filtering — be ruthless

The AIOS may read the inbox, but this skill **reports almost none of it**.
Surface an item only if it matches one of the criteria in
`Konfig → Morgens prüfen` → *Mail-Filter*. Everything else is inbox work, and
inbox work is not a morning briefing. If nothing qualifies, say *"Nothing
overnight that changes today"* and move on.

## Output shape

Aim for something the user can read standing up. Example — invented, not the
configured case; the second line is whatever plan line the configuration
defines:

```
Thursday 18 August

Focus — Shop: autumn catalogue proofed and sent to the printer.
Daily step — call the printer, confirm the price.

  09:00–11:00  Shop — catalogue proof
  19:00–20:00  Team call  (fixed)

Accountant replied — wants last year's figures by Friday.

Still the plan?
```

Speak in the language set in `Konfig → Kopf`. No preamble, no greeting beyond
the date, no closing encouragement. If it runs past roughly fifteen lines, it is
too long — cut the mail section first.

## Never do here

- Never re-plan the whole day. That is `/day-close`.
- Never dump the inbox.
- Never guilt-trip about a skipped evening or a missed block.
- Never write calendar blocks from scratch — `/day-close` creates them, this one
  only adjusts.
- Never read or plan anything listed under `Konfig → Nie im Tagesritual`.
- Never end a turn on a tool call when the text before it is for the user — the
  text would not be shown. Read first, then speak.
