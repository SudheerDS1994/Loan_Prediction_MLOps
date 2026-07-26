import pandas as pd
import numpy as np
from evidently.metric_preset import DataDriftPreset
from evidently.report import Report
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DriftDetector:
    """Detect data drift using Evidently"""
    
    def __init__(self, threshold=0.5):
        self.threshold = threshold
    
    def detect_drift(self, reference_df, current_df):
        """Detect data drift"""
        try:
            report = Report(metrics=[DataDriftPreset()])
            report.run(reference_data=reference_df, current_data=current_df)
            
            # Extract drift status
            drift_detected = report.as_dict()['metrics'][0]['result']['drift_detected']
            logger.info(f"Drift detected: {drift_detected}")
            
            return drift_detected
        except Exception as e:
            logger.error(f"Error detecting drift: {str(e)}")
            return False
    
    def get_drift_report(self, reference_df, current_df):
        """Get detailed drift report"""
        try:
            report = Report(metrics=[DataDriftPreset()])
            report.run(reference_data=reference_df, current_data=current_df)
            return report
        except Exception as e:
            logger.error(f"Error generating drift report: {str(e)}")
            return None