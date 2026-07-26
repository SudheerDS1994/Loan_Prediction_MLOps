import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def evaluate_predictions(y_true, y_pred, y_pred_proba=None):
    """Comprehensive model evaluation"""
    
    logger.info("Generating evaluation report...")
    
    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    logger.info(f"Confusion Matrix:\n{cm}")
    
    # Classification Report
    report = classification_report(y_true, y_pred)
    logger.info(f"Classification Report:\n{report}")
    
    # ROC-AUC
    if y_pred_proba is not None:
        roc_auc = roc_auc_score(y_true, y_pred_proba)
        logger.info(f"ROC-AUC Score: {roc_auc}")
    
    return cm, report