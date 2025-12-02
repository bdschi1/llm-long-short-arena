# Scenario Notes (LLM Long–Short Arena)

This folder contains the initial scenarios used to stage duels between a
Long PM and a Short PM:

- `ai_infra_vs_productivity_rotation_event_path.md`
- `crowded_shared_favorites_drawdown_event_path.md`

Both are designed to stress the same core ideas:

1. **Risk as the budgeting currency**
   - Each scenario forces the PM to decide how much of a finite risk budget
     to allocate to a theme (AI infra vs productivity, or crowded quality
     winners), not just whether an idea is “good” or “bad”.
   - The focus is on marginal risk and alpha per unit of incremental risk,
     not just direction.

2. **Event paths instead of static price targets**
   - Scenarios are structured as **event paths** (earnings, guidance,
     corporate commentary, flows/positioning, macro shocks).
   - The Long PM and Short PM must explain how conviction and position size
     change along these paths, rather than giving a single target and horizon.

3. **Conviction levers and conviction trajectory**
   - Each scenario surfaces key **conviction levers** (e.g., AI demand vs
     productivity gains, crowding vs fundamentals) and asks how new
     information shifts conviction and sizing, even if the thesis direction
     does not flip.
   - Over multiple iterations, the goal is to track how conviction evolves
     across thesis components (growth, margins, positioning, risk).

These scenarios are intentionally stylized and synthetic. They are meant to:

- Be simple enough to run with different models and prompts.
- Be rich enough to reveal differences in **reasoning, risk awareness,
  and portfolio usage** between models.
- Provide a clear link back to the evaluation rubric in `evals/` and the
  Long/Short PM system prompts in `prompts/`.

Additional scenarios can be added later following the same pattern:
clear setup, explicit event path, and well-defined conviction levers.
