# src/judge.py
import os
from openai import OpenAI
from src.schemas import CIOVerdict

class Judge:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def adjudicate(self, long_data, short_data):
        """
        Compares the Long and Short outputs to render a final verdict.
        """
        system_prompt = """
        You are the Chief Investment Officer (CIO) of a multi-manager hedge fund.
        Two of your Senior PMs (Long and Short) have just pitched you on the same name.
        
        YOUR GOAL:
        1. Synthesize their arguments into a final trading decision.
        2. Determine the 'Net Risk Units' (Long Units minus Short Units, adjusted for conviction).
        3. Identify the 'Deciding Factor'—why did you side with one over the other?
        
        CRITICAL: 
        - If the Long Thesis relies on 'Hope' but the Short Thesis relies on 'Math', side with the Short.
        - If the Short Thesis ignores a fundamental catalyst, side with the Long.
        """

        user_content = f"""
        🔵 LONG PM PITCH:
        Risk Units: {long_data.risk_sizing.risk_units}
        Thesis: {long_data.thesis_summary}
        Key Drivers: {long_data.key_drivers}
        
        🔴 SHORT PM PITCH:
        Risk Units: {short_data.risk_sizing.risk_units}
        Thesis: {short_data.thesis_summary}
        Key Drivers: {short_data.key_drivers}
        """

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            response_format=CIOVerdict
        )
        return completion.choices[0].message.parsed