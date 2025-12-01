# Long–Short Arena Evaluation Rubric

This rubric is used to evaluate two model outputs generated for the same
scenario:

- **Long PM** – argues for owning / being long the name or portfolio.
- **Short PM** – argues for being short, underweight, or avoiding it.
- **Long/Short PM** – may hold both long and short positions in the same
  book, but must still articulate the long and short sides of the idea.

The “arena” compares how well each role reasons about the same scenario.

---

## Context & Goals

The mindset behind this rubric is that, in a long/short equity book, **risk
is the fundamental budgeting currency**. You think in units of risk, not
just dollars or notional: every position consumes a slice of a finite risk
budget, measured consistently (e.g., factor, idiosyncratic, and convexity
risk contributions).

The goal is to:

- Decompose risk into additive slices (factors, sectors, styles, single
  names, legs of pairs, tail scenarios).
- Size and trim so each slice has an explicit role and capped contribution
  to total volatility and drawdown.
- Judge whether the model’s long/short reasoning behaves like this, rather
  than letting risk emerge as an accident of ideas.

We evaluate both:

1. The quality of each side’s **reasoning**.
2. How well each side **identifies, weighs, and responds to features that
   change investment conviction and sizing**.
3. How conviction evolves across **iterations** and across different
   components of the thesis.

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
- 5 – Surfaces idiosyncratic, sector, and macro risks and links them to thesis,
      sizing, and portfolio-level risk.

---

## 4. Conviction Levers (Features That Change Conviction & Sizing)

**Question:** Does the PM correctly identify and weight the *features that
move conviction and position size up or down*?

Examples of conviction levers:

- New information that would **upgrade/downgrade conviction** or change
  risk/reward (even if the thesis direction stays the same).
- KPI trajectories (e.g., churn, unit economics, pricing power).
- Balance sheet or liquidity changes.
- Competitive or regulatory developments.
- R&D projects with path-dependent outcomes (e.g., clinical trials for
  biotech, new chip development for AI hardware) and milestone risk.
- For portfolios: factor exposures, correlations, concentration changes, and
  the impact of **position size itself** as a risk lever.

Scoring:

- 1 – Barely addresses what would change conviction or size; mostly static views.
- 3 – Mentions some levers but does not clearly prioritize or tie them to
  position size and risk/reward.
- 5 – Explicitly lists the main conviction drivers, ranks them, and explains
  how each would change thesis confidence and position size
  (e.g., “If X happens, I cut from 4% to 2%; if Y happens, I add to 5%”).

---

## 5. Positioning & Risk Use

**Question:** Does the PM translate thesis + conviction into sensible
position sizing and risk usage, in risk units rather than just dollars?

- 1 – No sizing logic; just “buy/sell” with no relation to risk.
- 3 – Basic sizing logic (“small starter,” “core position”) but limited link
  to volatility, drawdown, factor and idiosyncratic contributions.
- 5 – Clear sizing framework tied to:
  - The idea’s role in the book (alpha source, hedge, pair leg),
  - Its contribution to factor, idiosyncratic, and convexity risk,
  - Gross, net, and factor exposures expressed in “risk units,” and
  - Alpha per unit of marginal risk (capital flows to best ideas per
    incremental risk budget).

High-scoring answers make it clear that risk is budgeted deliberately and
continuously rebalanced, not discovered after the fact.

---

## 6. Reasoning Quality & Internal Consistency

**Question:** Is the argument logically coherent?

- 1 – Contradictions, hand-waving, or unexplained leaps.
- 3 – Mostly coherent; some gaps or ambiguous steps.
- 5 – Step-by-step reasoning with explicit assumptions and clear
      “because → therefore” structure.

---

## 7. Event Path & Path-Dependent Conviction

**Question:** Does the PM articulate a clear **event path** for the idea and
how conviction changes along that path?

- 1 – No real event path; just a target price or vague time horizon.
- 3 – Some notion of events (earnings, trial readouts, product launches) but
      limited clarity on how each event affects conviction and sizing.
- 5 – Explicit event paths to target or exit (e.g., “Q+1 results, trial
      milestones, regulatory decisions”) and clear statements of how new
      information along each path would change conviction and sizing across
      the thesis components.

High-scoring answers treat event paths as first-class objects in the thesis.

---

## 8. Comparative Outcome: Which Side “Wins”?

After scoring both Long PM and Short PM on all dimensions, the evaluator
selects a winner for the scenario.

Baseline approach:

- Compute overall scores (e.g., simple or weighted average of dimensions).
- Use those scores to identify which side is stronger.

Then overlay qualitative judgment:

- **Long wins** – Long thesis better reasoned and conviction/risk handling
  is superior.
- **Short wins** – Short thesis is stronger on the same basis.
- **Split decision** – Both sides are roughly equal, or one is better on
  thesis but the other is better on risk/conviction/event-path handling.

The evaluator should record:

- The dimension(s) that drove the decision (often Conviction Levers,
  Positioning & Risk Use, and Event Path).
- Any **critical missing feature** (e.g., a KPI or event) that would have
  changed the winner if recognized by the model.

---

## 9. Logging (Single Snapshot)

For each duel (even if you only look at a final output), record in a simple
table or JSON:

- Scenario ID
- Model / configuration for Long PM
- Model / configuration for Short PM
- Scores by dimension for each side
- Winner and reason (short text)
- Notes on failure modes, especially around conviction levers, event paths,
  and risk usage

---

## 10. Conviction Trajectory Across Iterations (Optional but Recommended)

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
- Adjust conviction differently across parts of the thesis.
- Avoid pathological behavior such as overreacting to minor points or
  ignoring major new evidence.

A simple logging schema (manually or in CSV/JSON) might include:

- Scenario ID
- Role (Long PM / Short PM / Long/Short PM)
- Iteration number
- Thesis component (e.g., Growth, Margins, Balance Sheet, Regulation)
- Conviction score (1–5 or Low/Med/High)
- Direction of change (Up / Down / Flat)
- Short reason for change
