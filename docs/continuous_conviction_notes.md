# Notes: Continuous / Bayesian Conviction (Placeholder)

This document is a placeholder for future work on moving from discrete
(1–5) scores to **continuous and Bayesian-style conviction tracking** in the
long–short arena.

Conceptual direction:

- Treat conviction as a continuous variable (e.g., a probability or log-odds)
  rather than a discrete bucket.
- Update conviction as new information arrives:
  - Fundamentals (earnings, guidance, KPIs)
  - Price action and volatility
  - Portfolio context (factor moves, drawdowns, concentration)
- Map conviction and expected alpha into **risk units**, not just notional
  dollars, so each position consumes part of a finite risk budget in the
  long/short book.
- Use simple Bayesian-style updates as a conceptual model: prior conviction,
  new signal with some reliability, posterior conviction → updated position
  size and risk contribution.

This is intentionally skeletal for now and will be expanded once initial
discrete rubrics, scenarios, and prompts are in place.
