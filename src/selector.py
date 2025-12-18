import os
from openai import OpenAI
from src.schemas import TradeTarget

class Selector:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def select_target(self, text: str) -> TradeTarget:
        """
        Analyzes the text to pick the best trading vehicle (Stock or ETF).
        """
        system_prompt = """
        You are a Senior Research Analyst at a Hedge Fund.
        
        YOUR TASK:
        Analyze the provided research document and identify the SINGLE BEST trading instrument 
        to express the views contained within.
        
        LOGIC:
        1. **Single Name Report?** -> Return that specific Ticker.
        2. **Sector/Macro Report?** -> You must pick the best **LIQUID PROXY** (ETF or Bellwether Stock).
           - Example: If report is "The Future of AI Hardware", pick **NVDA** or **SMH**.
           - Example: If report is "Biotech Primer", pick **XBI** (SPDR Biotech ETF).
           - Example: If report is "Rates are falling", pick **TLT**.
        
        CONSTRAINT:
        - Do not pick obscure, illiquid stocks. 
        - If multiple options exist, pick the one with the highest beta to the theme.
        """

        try:
            completion = self.client.beta.chat.completions.parse(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Analyze this research:\n\n{text[:20000]}"} 
                ],
                response_format=TradeTarget,
            )
            return completion.choices[0].message.parsed
        except Exception as e:
            print(f"Selection Error: {e}")
            # Fallback default
            return TradeTarget(
                is_sector_report=True, 
                primary_ticker="SPY", 
                instrument_name="S&P 500", 
                reasoning="Fallback: Could not identify specific target.", 
                confidence=1
            )