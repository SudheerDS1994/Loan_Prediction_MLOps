import streamlit as st
import pandas as pd
import numpy as np
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="Loan Prediction Monitoring", layout="wide")

@st.cache_resource
def load_reference_data():
    """Load reference dataset for drift comparison"""
    try:
        df = pd.read_csv('data/train.csv')
        return df
    except FileNotFoundError:
        st.error("Reference data not found")
        return None

@st.cache_resource
def load_current_data():
    """Load current dataset for comparison"""
    try:
        df = pd.read_csv('data/test.csv')
        return df
    except FileNotFoundError:
        st.warning("Current data not found. Using reference data.")
        return load_reference_data()

def calculate_data_drift(reference_df, current_df):
    """Calculate data drift using Evidently"""
    try:
        report = Report(metrics=[DataDriftPreset()])
        report.run(reference_data=reference_df, current_data=current_df)
        return report
    except Exception as e:
        logger.error(f"Error calculating drift: {str(e)}")
        st.error(f"Error calculating drift: {str(e)}")
        return None

def calculate_data_quality(reference_df, current_df):
    """Calculate data quality using Evidently"""
    try:
        report = Report(metrics=[DataQualityPreset()])
        report.run(reference_data=reference_df, current_data=current_df)
        return report
    except Exception as e:
        logger.error(f"Error calculating quality: {str(e)}")
        st.error(f"Error calculating quality: {str(e)}")
        return None

def main():
    st.title("🔍 Loan Prediction - Data Monitoring Dashboard")
    
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Choose an option",
        ["Home", "Data Drift", "Data Quality", "Statistics"]
    )
    
    # Load data
    reference_df = load_reference_data()
    current_df = load_current_data()
    
    if reference_df is None:
        st.error("Unable to load data. Please ensure data files exist.")
        return
    
    # Home Page
    if page == "Home":
        st.markdown("""
        ### 📊 Welcome to Loan Prediction Monitoring
        
        This dashboard provides comprehensive monitoring for the loan prediction model:
        
        - **Data Drift**: Monitor if data distribution has changed significantly
        - **Data Quality**: Track data quality metrics and anomalies
        - **Statistics**: View detailed statistical analysis
        
        Use the sidebar to navigate between sections.
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Reference Dataset Size", len(reference_df))
        with col2:
            st.metric("Current Dataset Size", len(current_df))
        with col3:
            st.metric("Features", reference_df.shape[1])
    
    # Data Drift Page
    elif page == "Data Drift":
        st.header("📈 Data Drift Analysis")
        st.write("Analyzing if the data distribution has changed...")
        
        if st.button("Calculate Data Drift"):
            with st.spinner("Calculating data drift..."):
                drift_report = calculate_data_drift(reference_df, current_df)
                
                if drift_report:
                    st.success("Data drift calculation completed!")
                    
                    # Save report
                    drift_report.save_html("drift_report.html")
                    
                    # Display report
                    with open("drift_report.html", "r") as f:
                        st.components.v1.html(f.read(), height=800, scrolling=True)
                else:
                    st.error("Failed to calculate data drift")
    
    # Data Quality Page
    elif page == "Data Quality":
        st.header("✅ Data Quality Analysis")
        st.write("Checking data quality metrics...")
        
        if st.button("Calculate Data Quality"):
            with st.spinner("Calculating data quality..."):
                quality_report = calculate_data_quality(reference_df, current_df)
                
                if quality_report:
                    st.success("Data quality calculation completed!")
                    
                    # Save report
                    quality_report.save_html("quality_report.html")
                    
                    # Display report
                    with open("quality_report.html", "r") as f:
                        st.components.v1.html(f.read(), height=800, scrolling=True)
                else:
                    st.error("Failed to calculate data quality")
    
    # Statistics Page
    elif page == "Statistics":
        st.header("📊 Data Statistics")
        
        tab1, tab2 = st.tabs(["Reference Data", "Current Data"])
        
        with tab1:
            st.subheader("Reference Dataset Statistics")
            st.write(reference_df.describe())
            
            st.subheader("Reference Data Info")
            st.write(f"Shape: {reference_df.shape}")
            st.write(f"Missing values:\n{reference_df.isnull().sum()}")
        
        with tab2:
            st.subheader("Current Dataset Statistics")
            st.write(current_df.describe())
            
            st.subheader("Current Data Info")
            st.write(f"Shape: {current_df.shape}")
            st.write(f"Missing values:\n{current_df.isnull().sum()}")

if __name__ == "__main__":
    main()