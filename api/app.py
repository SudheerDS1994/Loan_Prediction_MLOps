from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import logging
from prometheus_client import Counter, Histogram, generate_latest
import time
from api.schemas import PredictionRequest, PredictionResponse, HealthCheckResponse

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Loan Prediction API",
    description="API for loan prediction model",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prometheus metrics
prediction_counter = Counter(
    'predictions_total',
    'Total predictions',
    ['result']
)

prediction_latency = Histogram(
    'prediction_latency_seconds',
    'Prediction latency in seconds'
)

approved_predictions = Counter(
    'approved_predictions',
    'Number of approved loans'
)

rejected_predictions = Counter(
    'rejected_predictions',
    'Number of rejected loans'
)

@app.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """Health check endpoint"""
    return HealthCheckResponse(
        status="healthy",
        version="1.0.0"
    )

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Make loan prediction"""
    start_time = time.time()
    
    try:
        logger.info(f"Received prediction request: {request}")
        
        # Simple prediction logic (replace with actual model)
        # For demo: approve if income > 3000 and credit_score > 650
        features = np.array([
            request.age,
            request.income,
            request.credit_score,
            request.loan_amount,
            request.employment_years
        ]).reshape(1, -1)
        
        # Simple rule-based prediction for demo
        if request.income > 3000 and request.credit_score > 650:
            prediction = 1
            probability = 0.85
            approved = True
        else:
            prediction = 0
            probability = 0.15
            approved = False
        
        # Update metrics
        latency = time.time() - start_time
        prediction_latency.observe(latency)
        prediction_counter.labels(result='success').inc()
        
        if approved:
            approved_predictions.inc()
        else:
            rejected_predictions.inc()
        
        logger.info(f"Prediction: {prediction}, Approved: {approved}")
        
        return PredictionResponse(
            prediction=prediction,
            probability=probability,
            approved=approved,
            confidence=probability
        )
    
    except Exception as e:
        prediction_counter.labels(result='error').inc()
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint"""
    return generate_latest()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Loan Prediction API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "predict": "/predict",
            "metrics": "/metrics"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)