#!/bin/bash

# Script to set up the entire MLOps project

echo "====================================="
echo "MLOps Project Setup Script"
echo "====================================="

# Check Python version
echo "Checking Python version..."
python --version

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate || . venv/Scripts/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Initialize DVC
echo "Initializing DVC..."
dvc init --no-scm || true

# Initialize MLflow tracking
echo "Setting up MLflow..."
export MLFLOW_TRACKING_URI=http://localhost:5001

# Create necessary directories
echo "Creating directories..."
mkdir -p data models logs mlruns

echo "====================================="
echo "Setup completed successfully!"
echo "====================================="
echo ""
echo "Next steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Train the model: python model/train.py"
echo "3. Start MLflow UI: mlflow ui --host 0.0.0.0 --port 5001"
echo "4. Run the API: python api/app.py"
echo "5. Monitor data drift: streamlit run monitoring/app.py"
