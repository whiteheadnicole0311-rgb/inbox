# Tidal — PAH & Remodulin care tracker

A single-file web app for tracking pulmonary arterial hypertension (PAH) in a
way that's easy to log day-to-day but stays meaningful to a care team, plus
medication (including dose change history) and IV/specialty-pharmacy supply
tracking.

**Live app:** https://claude.ai/code/artifact/a17f97de-c5f6-452f-b786-a357f4e261df

## What it does

- **Dashboard** — reorder alerts, last check-in, WHO functional class, weight
  and 6-minute-walk trend, active medications, and supply status at a glance.
- **Check-in** — WHO functional class, 6MWT distance, vitals (O2 sat at rest
  and exertion, heart rate, blood pressure, weight), symptom severity
  (dyspnea, fatigue, edema, chest pain, dizziness, palpitations), and an
  infusion-site/pump-alarm check. Full editable history below the form.
- **Medications** — current medication list (dose, route, frequency,
  prescriber) plus a change log that records every dose/medication change
  with a reason, and updates the current dose automatically.
- **Supplies** — the 18 items you use for IV Remodulin therapy, pre-loaded
  with editable on-hand quantities and reorder thresholds, grouped by
  category, with a reorder banner and an "add new supply" form for anything
  else you need to track.
- **Report** — a date-ranged summary built to hand to your care team: trend
  stats, current meds, changes in range, the full check-in log, and supplies
  needing reorder. Print/save as PDF, or export CSVs.

## How it's built

Plain HTML/CSS/JS, no build step. Data is stored in the artifact's built-in
database (the `db` runtime capability), so it persists across devices and
sessions for anyone who opens the live app link above — there is no separate
backend to run. Opening `index.html` directly (outside claude.ai) will render
the UI but without persistence, since the `db` capability isn't available
there.
