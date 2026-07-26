import pytest
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

@pytest.fixture
def sample_data():
    """Create sample data for testing"""
    X, y = make_classification(n_samples=100, n_features=5, random_state=42)
    return X, y

def test_model_training(sample_data):
    """Test model training"""
    X, y = sample_data
    model = LogisticRegression()
    model.fit(X, y)
    
    assert model.coef_ is not None
    assert len(model.coef_[0]) == 5

def test_model_prediction(sample_data):
    """Test model prediction"""
    X, y = sample_data
    model = LogisticRegression()
    model.fit(X, y)
    
    predictions = model.predict(X[:10])
    assert len(predictions) == 10
    assert all(pred in [0, 1] for pred in predictions)

def test_model_prediction_proba(sample_data):
    """Test model probability predictions"""
    X, y = sample_data
    model = LogisticRegression()
    model.fit(X, y)
    
    probabilities = model.predict_proba(X[:10])
    assert probabilities.shape == (10, 2)
    assert all(0 <= prob <= 1 for row in probabilities for prob in row)