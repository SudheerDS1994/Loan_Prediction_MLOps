#!/bin/bash

# Script to run all tests

echo "====================================="
echo "Running All Tests"
echo "====================================="

# Activate virtual environment
source venv/bin/activate || . venv/Scripts/activate

# Run pytest
echo "Running pytest..."
pytest tests/ -v --cov=api --cov=model --cov-report=html --cov-report=term

echo ""
echo "Test report generated in htmlcov/index.html"
