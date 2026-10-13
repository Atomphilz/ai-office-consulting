# Daily file template

The shape of every file in the daily folder (`references/tagesritual.md` →
`## Werkzeuge` → Tagesdatei; `daily/` by default). **Both** `/day-close` and
`/day-open` write files in this format, so the template lives here rather than
inside either skill:

- `/day-close` writes tomorrow's file from this template every evening.
- `/day-open` writes today's file from this template on a cold start, when the
  evening before was skipped.

Keep the headings exactly as written. `/day-open` reads `## Focus`, `## Blocks`
and `## Fixed` by heading, and `/day-close` appends under `## Evening review`.
The two placeholders marked *from the configuration* are filled from
`references/tagesritual.md` → `## Abends erfassen` → *Zeilen in der
Tagesdatei*; everything else is fixed.

---

```markdown
# <Weekday> <D Month YYYY>

## Focus
<One sentence. Which area, and what done looks like.>

<Plan lines from the configuration, plan part, each on its own line. Omit
entirely if the configuration lists none.>

## Blocks
- 09:00–11:00 — <Area> — <what>
- 14:00–15:00 — <Area> — <what>

## Carried over
- <commitments and loose ends from the evening capture>

## Fixed
- <calendar events already on the day>

## Trade-off accepted
<What the day is NOT doing, and which priority pays for it. One line.
Omit only if there genuinely was no conflict.>

---
## Evening review — <filled that evening by /day-close>

**What happened:**

<Capture lines from the configuration, evening part, in the order given there.
Each is written as `**<label>:** <value>`; "none" rather than blank. Omit
entirely if the configuration lists none.>

**Promised to someone:**
```

---

## Why each file holds both halves

The plan goes in at the top the night before; the honest post-mortem gets
appended to the same file the following evening. One file per day, containing
both what was intended and what actually happened — which is what makes drift
visible when you read a week of them side by side.

`/day-close` therefore touches **two** files each evening: it appends the review
to today's file, then creates tomorrow's.

## Where the area focus comes from

Free choice from the areas listed in `references/tagesritual.md` →
`## Bereiche`, proposed by the skill and picked by the user. Whether a fixed
weekday-to-area map exists is that section's call; by default there is none.
