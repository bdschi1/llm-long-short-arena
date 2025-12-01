# Long–Short Arena Evaluation Rubric

This rubric is used to evaluate two model outputs generated for the same
scenario:

- **Long PM** – argues for owning / being long the name or portfolio.
- **Short PM** – argues for being short, underweight, or avoiding it.

The goal is to evaluate:

1. The quality of each side’s **reasoning**.
2. How well each side **identifies, weighs, and responds to features that
   change investment conviction** (both thesis and position size).
3. How conviction evolves across **iterations** of analysis and across
   different parts of the thesis.

Scores are given on a 1–5 scale for each dimension.

---

## 1. Factual Grounding

**Question:** Is the thesis anchored in the scenario facts provided?

- 1 – Multiple material factual errors or fabrications.
- 3 – Mostly accurate; minor slips that do not change the conclusion.
- 5 – No material factual errors; clearly grounded in the scenario notes.

---

## 2. Business & Driver Understanding

**Question:** Does the PM understand how this company/portfolio actually
makes and loses money?

- 1 – Superficial; generic commentary that could fit any name.
- 3 – Correct core drivers but limited nuance (e.g., one or two key KPIs missed).
- 5 – Clear mapping from business model → KPIs → earnings/cash flow → valuation.

---

## 3. Risk Awareness

**Question:** Does the PM identify and weigh key risks?

- 1 – Ignores obvious risks a human PM would flag immediately.
- 3 – Identifies some important risks but misses others or treats them shallowly.
- 5 – Surfaces idiosyncratic, sector, and macro risks and links them to thesis
      and sizing.

---

## 4. Conviction Levers (Features That Change Conviction)

**Question:** Does the PM correctly identify and weight the *features that
move conviction up or down*?

Examples of conviction levers:

- New information that would **upgrade/downgrade** the thesis.
- KPI trajectories (e.g., churn, unit economics, pricing power).
- Balance sheet or liquidity changes.
- Competitive or regulatory developments.
- For portfolios: factor exposures, correlations, concentration changes.

Scoring:

- 1 – Barely addresses what would change conviction; mostly static views.
- 3 – Mentions some levers but does not clearly prioritize them or quantify impact.
- 5 – Explicitly lists the main conviction drivers, ranks them, and explains
      how each would change thesis and position size (“If X happens, I cut
      from 4% to 2%,” etc.).

---

## 5. Positioning & Risk Use

**Question:** Does the PM translate thesis + conviction into sensible position
sizing and risk constraints?

- 1 – No sizing logic; just “buy/sell.”
- 3 – Basic sizing logic (“small starter,” “core position”) but limited detail.
- 5 – Clear sizing framework tied to conviction, liquidity, portfolio role,
      and risk limits (e.g., max drawdown, stop-loss, pair structure).

---

## 6. Reasoning Quality & Internal Consistency

**Question:** Is the argument logically coherent?

- 1 – Contradictions, hand-waving, or unexplained leaps.
- 3 – Mostly coherent; some gaps or ambiguous steps.
- 5 – Step-by-step reasoning with explicit assumptions and clear “because → therefore”
      structure.

---

## 7. Comparative Outcome: Which Side “Wins”?

After scoring both Long PM and Short PM on all dimensions, the evaluator
selects a winner for the scenario:

- **Long wins** – Long thesis better reasoned and conviction levers are
  better identified/weighted.
- **Short wins** – Short thesis is stronger on the same basis.
- **Split decision** – Both sides are roughly equal, or one is better on
  thesis but the other is better on risk/conviction handling.

The evaluator should record:

- The dimension(s) that drove the decision (often Conviction Levers + Risk).
- Any **critical missing feature** (e.g., a KPI or event) that would have
  changed the winner if recognized by the model.

---

## 8. Logging (Single Snapshot)

For each duel (even if you only look at a final output), record in a simple
table or JSON:

- Scenario ID
- Model / configuration for Long PM
- Model / configuration for Short PM
- Scores by dimension for each side
- Winner and reason (short text)
- Notes on failure modes, especially around conviction levers

---

## 9. Conviction Trajectory Across Iterations (Optional but Recommended)

Beyond a single snapshot, you can track how each side’s conviction evolves
over **major iterations** of analysis (e.g., as new facts, counterarguments,
or scenarios are introduced).

For each iteration, and for each major component of the thesis (e.g.,
“top-line growth,” “unit economics,” “regulation,” “competition”), record:

- A **conviction score** (e.g., 1–5, or Low/Med/High).
- Whether conviction moved **up, down, or unchanged** vs the prior iteration.
- A short note on *why* (what new feature or argument changed it, if any).

This lets you evaluate whether the model can:

- Update conviction appropriately when new information arrives.
- Adjust conviction differently across parts of the thesis (e.g., more confident
  on growth, less confident on margins).
- Avoid pathological behavior such as overreacting to minor points or ignoring
  major new evidence.

A simple logging schema (manually or in CSV/JSON) might include:

- Scenario ID
- Role (Long PM / Short PM)
- Iteration number
- Thesis component (e.g., Growth, Margins, Balance Sheet, Regulation)
- Conviction score (1–5 or Low/Med/High)
- Direction of change (Up / Down / Flat)
- Short reason for change
