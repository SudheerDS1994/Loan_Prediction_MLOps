import pytest
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_approved():
    """Test prediction for approved loan"""
    payload = {
        "age": 45,
        "income": 5000,
        "credit_score": 700,
        "loan_amount": 20000,
        "employment_years": 5
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "probability" in data
    assert "approved" in data

def test_predict_rejected():
    """Test prediction for rejected loan"""
    payload = {
        "age": 25,
        "income": 1000,
        "credit_score": 500,
        "loan_amount": 50000,
        "employment_years": 1
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["approved"] == False

def test_metrics_endpoint():
    """Test metrics endpoint"""
    response = client.get("/metrics")
    assert response.status_code == 200