from pydantic import BaseModel
from typing import Optional

class PredictionRequest(BaseModel):
    """Request schema for loan prediction"""
    age: int
    income: float
    credit_score: int
    loan_amount: float
    employment_years: int

class PredictionResponse(BaseModel):
    """Response schema for loan prediction"""
    prediction: int
    probability: float
    approved: bool
    confidence: float

class HealthCheckResponse(BaseModel):
    """Health check response"""
    status: str
    version: str