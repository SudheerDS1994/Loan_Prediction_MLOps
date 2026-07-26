import logging
import numpy as np
from typing import List, Dict

logger = logging.getLogger(__name__)

def validate_features(features: Dict) -> bool:
    """Validate input features"""
    required_fields = ['age', 'income', 'credit_score', 'loan_amount', 'employment_years']
    
    for field in required_fields:
        if field not in features:
            logger.warning(f"Missing required field: {field}")
            return False
    
    return True

def normalize_features(features: np.ndarray) -> np.ndarray:
    """Normalize input features"""
    return (features - features.mean()) / features.std()

def format_prediction(prediction: int, probability: float) -> Dict:
    """Format prediction output"""
    return {
        "prediction": int(prediction),
        "probability": float(probability),
        "approved": bool(prediction),
        "confidence": float(probability)
    }