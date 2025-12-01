# LLM Long–Short Arena

This repo runs structured “duels” between two large language models (or two
agent configurations) acting as a **long-side PM** and a **short-side PM**
on the same company or portfolio scenario.

The goal is not to auto-trade, but to see whether models can produce
decision-useful, risk-aware long and short theses that resemble what a
professional investor would write.

---

## Concept

For each scenario:

- One model is assigned the role of **Long PM**.
- Another model is assigned the role of **Short PM**.
- Both receive the same input package (e.g., earnings summary, KPIs, simple
  financials, and a description of recent price action).
- Each side must:
  - State a thesis (long or short),
  - Identify key drivers and risks,
  - Propose position sizing / risk constraints,
  - Explain what evidence would change their mind.

Evaluation focuses on both **reasoning quality** and how well each side
**identifies and weights the features that change investment conviction**
(what would make you add, cut, or reverse the position).

---

## Repo structure

Planned layout:

- `data/` – Simple, synthetic or public scenarios describing companies or
  small portfolios (no confidential data).
- `prompts/` – System and user prompts used for the Long PM and Short PM roles.
- `evals/` – Rubrics and scoring guidelines for comparing outputs.
- `notebooks/` – Worked examples and manual comparisons. Code-driven
  experiments can be added over time.

---

## Intended audience

This project is aimed at:

- Investment teams exploring how LLMs behave in long/short workflows.
- AI / ML teams who want domain-specific evaluation scenarios, not generic benchmarks.
- AI trainer / evaluator roles that need to design and score realistic PM-style tasks.

---

## Status

Early-stage, starting with:

1. A single earnings-related scenario.
2. Role prompts for Long PM and Short PM.
3. A manual, rubric-based comparison of model outputs.

Future iterations may add:

- Multiple models and agent frameworks.
- Automated scoring scripts.
- More sectors (e.g., healthcare, tech) and more complex portfolio cases.
