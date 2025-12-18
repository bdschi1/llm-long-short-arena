import os
from openai import OpenAI
from src.schemas import PMAnalysis

class Arena:
    def __init__(self):
        # Ensure your API Key is set in your environment
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def _load_prompt(self, filename: str) -> str:
        # Looks for prompts in the src/prompts folder
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "prompts", filename)
        
        if not os.path.exists(path):
            raise FileNotFoundError(f"Prompt file not found: {path}")
            
        with open(path, "r") as f:
            return f.read()

    def run_agent(self, role: str, scenario: str) -> PMAnalysis:
        """
        Runs a single agent (Long or Short) against the scenario.
        """
        print(f"🤖 Activating {role}...")
        
        # Select the correct system prompt file
        prompt_file = "long_pm.md" if role == "Long" else "short_pm.md"
        system_prompt = self._load_prompt(prompt_file)

        try:
            completion = self.client.beta.chat.completions.parse(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Here is the market scenario:\n\n{scenario}"}
                ],
                response_format=PMAnalysis,
            )
            return completion.choices[0].message.parsed
        except Exception as e:
            print(f"❌ Error running {role}: {e}")
            return None

    def fight(self, scenario: str, target: str = None):
        """
        Runs the duel. 
        target: The specific Ticker (e.g. 'XBI') to focus the debate on.
        """
        print("\n🥊 --- STARTING DUEL --- 🥊\n")
        
        # We inject the Ticker into the prompt context dynamically
        context_enrichment = ""
        if target:
            context_enrichment = f"\n\n🚨 TRADING TARGET: {target}\nFocus your thesis specifically on {target} as the vehicle to express this view.\n"
        
        # Pass this enriched scenario to the agents
        full_scenario = context_enrichment + scenario
        
        long_output = self.run_agent("Long", full_scenario)
        short_output = self.run_agent("Short", full_scenario)
        
        return long_output, short_output