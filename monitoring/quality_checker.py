import pandas as pd
import numpy as np
from evidently.metric_preset import DataQualityPreset
from evidently.report import Report
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QualityChecker:
    """Check data quality using Evidently"""
    
    def __init__(self):
        pass
    
    def check_quality(self, reference_df, current_df):
        """Check data quality"""
        try:
            report = Report(metrics=[DataQualityPreset()])
            report.run(reference_data=reference_df, current_data=current_df)
            
            logger.info("Data quality check completed")
            return report
        except Exception as e:
            logger.error(f"Error checking quality: {str(e)}")
            return None
    
    def check_missing_values(self, df):
        """Check for missing values"""
        missing = df.isnull().sum()
        logger.info(f"Missing values:\n{missing}")
        return missing
    
    def check_outliers(self, df, columns, threshold=3):
        """Check for outliers using z-score"""
        outliers = {}
        for col in columns:
            z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
            outliers[col] = (z_scores > threshold).sum()
        logger.info(f"Outliers detected: {outliers}")
        return outliers