# Tidal — PAH & Remodulin care tracker

A single-file web app for tracking pulmonary arterial hypertension (PAH) in a
way that's easy to log day-to-day but stays meaningful to a care team, plus
medication (including dose change history) and IV/specialty-pharmacy supply
tracking.

**Live app:** https://claude.ai/code/artifact/a17f97de-c5f6-452f-b786-a357f4e261df

## What it does

- **Dashboard** — reorder alerts, last check-in, WHO functional class, weight
  and 6-minute-walk trend, active medications, and supply/packet status at a
  glance.
- **Check-in** — WHO functional class, 6MWT distance, weight with an
  automatic variance-since-last-entry calculation (flags rapid gain as a
  possible fluid-retention sign), vitals (O2 sat at rest and exertion, heart
  rate, blood pressure), breathing & heart symptoms (dyspnea, fatigue,
  orthopnea, cough, chest pain, palpitations, dizziness, syncope), fluid
  overload signs (edema, bloating), a medications-taken-today checklist
  pulled from your active medications, an activity & daily-life section, and
  an infusion-site/pump-alarm check. Full editable history below the form.
- **Medications** — current medication list (dose, route, frequency,
  prescriber); a **Remodulin mixing & titration calculator** — enter dosing
  weight, dose (ng/kg/min), mixed concentration, vial strength, and cassette
  volume to get the pump rate, mL of Remodulin/diluent, and cassette
  duration, with every titration kept in a history since the dose changes
  often; a **cassette label printer** that prints a filled-in 2×4in label
  (patient, prescriber, dose, mix, pump rate, mix/use-by date & time) sized
  for label stock; and a generic dose/medication change log for other
  medications.
- **Supplies** — a **complete-packet calculator** showing how many full
  dressing-change and cassette-change packets you can assemble right now
  from your loose supply counts (using each packet's real per-item
  quantities), plus the 18 loose items pre-loaded with editable on-hand
  quantities and reorder thresholds, grouped by category, with a reorder
  banner and an "add new supply" form.
- **Labs & Tests** — logs for Blood Work, Echo Results (with RVSP/TAPSE),
  Right Heart Cath (mPAP, PCWP, PVR, cardiac index, RAP), Functional Tests,
  and Imaging Studies.
- **Events** — a log for hospitalizations, ER visits, falls, infections,
  pump malfunctions, or anything else out of the ordinary, with start/end
  dates, location, description, and outcome.
- **Report** — a date-ranged summary built to hand to your care team: trend
  stats, current meds, changes in range, the full check-in log, complete
  packets on hand, and supplies needing reorder. Print/save as PDF, or
  export CSVs.

## How it's built

Plain HTML/CSS/JS, no build step. Data is stored in the artifact's built-in
database (the `db` runtime capability), so it persists across devices and
sessions for anyone who opens the live app link above — there is no separate
backend to run. Opening `index.html` directly (outside claude.ai) will render
the UI but without persistence, since the `db` capability isn't available
there.
