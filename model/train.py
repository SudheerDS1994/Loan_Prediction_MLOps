import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import mlflow
import mlflow.sklearn
import yaml
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_path="model/config.yaml"):
    """Load configuration from YAML file"""
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def load_data(config):
    """Load training data"""
    logger.info(f"Loading data from {config['data']['train_path']}")
    df = pd.read_csv(config['data']['train_path'])
    return df

def preprocess_data(df, config):
    """Preprocess and prepare data for training"""
    logger.info("Preprocessing data...")
    
    X = df[config['features']]
    y = df[config['data']['target_column']]
    
    # Handle missing values
    X = X.fillna(X.mean())
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=config['training']['test_size'],
        random_state=config['training']['random_state']
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    logger.info(f"Training set size: {X_train.shape}")
    logger.info(f"Test set size: {X_test.shape}")
    
    return X_train, X_test, y_train, y_test, scaler

def train_model(X_train, y_train, config):
    """Train logistic regression model"""
    logger.info("Training model...")
    
    params = config['training']['model_params']
    model = LogisticRegression(**params)
    model.fit(X_train, y_train)
    
    logger.info("Model training completed")
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance"""
    logger.info("Evaluating model...")
    
    y_pred = model.predict(X_test)
    
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred)
    }
    
    logger.info(f"Model Metrics: {metrics}")
    return metrics

def save_model(model, scaler, config):
    """Save model using MLflow"""
    logger.info("Saving model with MLflow...")
    
    mlflow.set_tracking_uri(config['mlflow']['tracking_uri'])
    mlflow.set_experiment(config['mlflow']['experiment_name'])
    
    with mlflow.start_run():
        # Log model
        mlflow.sklearn.log_model(model, "loan_predictor_model")
        
        # Log parameters
        for key, value in config['training']['model_params'].items():
            mlflow.log_param(key, value)
        
        logger.info("Model saved successfully with MLflow")

def main():
    """Main training pipeline"""
    config = load_config()
    
    # Load and preprocess data
    df = load_data(config)
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df, config)
    
    # Train model
    model = train_model(X_train, y_train, config)
    
    # Evaluate model
    metrics = evaluate_model(model, X_test, y_test)
    
    # Save model
    save_model(model, scaler, config)
    
    logger.info("Training pipeline completed successfully!")

if __name__ == "__main__":
    main()