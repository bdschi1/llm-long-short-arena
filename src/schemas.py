from pydantic import BaseModel, Field
from typing import List, Literal

class ConvictionLever(BaseModel):
    lever_name: str = Field(..., description="Name of the feature (e.g., 'Margins', 'FDA Approval')")
    impact_description: str = Field(..., description="How this specific lever changes sizing/conviction")
    sensitivity_score: int = Field(..., description="1-5: How sensitive is the thesis to this lever?")

class RiskSizing(BaseModel):
    risk_units: float = Field(..., description="Proposed size in Risk Units (1-10 scale)")
    role_in_book: Literal['Core', 'Tactical', 'Hedge', 'Pair Leg']
    max_drawdown_tolerance: str = Field(..., description="At what drawdown do you cut?")

class PMAnalysis(BaseModel):
    role: Literal['Long PM', 'Short PM']
    
    # --- NEW: THE ANALYTICAL JOURNEY ---
    analytical_process: str = Field(..., description="A step-by-step reasoning trace. Explain how you started with a baseline view and adjusted it based on specific evidence in the text. Walk through your logic.")
    
    thesis_summary: str = Field(..., description="5-10 bullet points summarizing the core view")
    key_drivers: List[str]
    risk_sizing: RiskSizing
    conviction_levers: List[ConvictionLever]
    event_path: List[str] = Field(..., description="Key milestones to watch over 6-18 months")
    confidence_score: int = Field(..., description="1-100 confidence score")

class TradeTarget(BaseModel):
    is_sector_report: bool = Field(..., description="True if macro/theme; False if single stock.")
    primary_ticker: str = Field(..., description="The single best Ticker to trade.")
    instrument_name: str
    reasoning: str
    confidence: int

class CIOVerdict(BaseModel):
    winner: str
    net_risk_units: float
    executive_summary: str
    deciding_factor: str