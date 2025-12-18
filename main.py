from src.arena import Arena
import json

# A Simple Test Scenario (Tesla-style Volatility)
TEST_SCENARIO = """
TICKER: TSLA (Hypothetical Context)
Price: $240. YTD Performance: +12%.
Context:
The company has just announced a delay in its Robotaxi rollout by 6 months. 
Margins in the core auto business compressed by 200bps YoY due to price cuts.
However, Energy storage revenue grew 100% YoY and is now 15% of total revenue.
CEO just sold $1B in stock for tax purposes.
Macro environment: Rates are expected to stay higher for longer.
"""

if __name__ == "__main__":
    arena = Arena()
    
    # Run the Duel
    long_res, short_res = arena.fight(TEST_SCENARIO)
    
    # Print Results
    if long_res and short_res:
        print("\n\n🔵 LONG PM DECISION:")
        print(f"Size: {long_res.risk_sizing.risk_units} Risk Units")
        print(f"Thesis: {long_res.thesis_summary[:200]}...")
        
        print("\n\n🔴 SHORT PM DECISION:")
        print(f"Size: {short_res.risk_sizing.risk_units} Risk Units")
        print(f"Thesis: {short_res.thesis_summary[:200]}...")
        
        # Save detailed JSON for debugging/grading
        with open("data/scenarios/duel_result.json", "w") as f:
            json.dump({
                "long": long_res.model_dump(), 
                "short": short_res.model_dump()
            }, f, indent=2)
            print("\n💾 Full detailed analysis saved to data/scenarios/duel_result.json")