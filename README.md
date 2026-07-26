# Loan Prediction MLOps Project

An end-to-end MLOps project demonstrating best practices for training, deploying, and monitoring a loan prediction model using modern DevOps and ML tools.

## 🎯 Project Overview

This project deploys a loan prediction model to assess customer loan eligibility with:
- **Automated model training** using scikit-learn
- **MLflow** for model versioning and tracking
- **DVC** for dataset versioning
- **Docker** for containerization
- **Jenkins** for CI/CD automation
- **Kubernetes** for orchestration and scaling
- **Prometheus & Grafana** for monitoring
- **Evidently AI** for data drift detection
- **Streamlit** for interactive data monitoring dashboard

## 📋 Prerequisites

- Python 3.8+
- Docker
- Kubernetes (kubectl configured)
- Jenkins
- Git
- DVC
- MLflow

## 🚀 Quick Start

### Step 1: Clone Repository
```bash
git clone https://github.com/SudheerDS1994/Loan_Prediction_MLOps.git
cd Loan_Prediction_MLOps
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Train Model
```bash
python model/train.py
mlflow ui --host 0.0.0.0 --port 5001
```

### Step 4: Run FastAPI Service
```bash
python api/app.py
```

### Step 5: Test API
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"age": 45, "income": 5000, "credit_score": 700, "loan_amount": 20000}' \
  http://127.0.0.1:8000/predict
```

### Step 6: Build Docker Image
```bash
docker build -t loan-predictor .
docker run -p 8000:8080 loan-predictor
```

### Step 7: Deploy to Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Step 8: Monitor with Streamlit
```bash
streamlit run monitoring/app.py
```

## 📁 Project Structure

```
Loan_Prediction_MLOps/
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── data.dvc
├── model/
│   ├── train.py
│   ├── evaluate.py
│   └── config.yaml
├── api/
│   ├── app.py
│   ├── schemas.py
│   └── utils.py
├── tests/
│   ├── test_model.py
│   └── test_api.py
├── monitoring/
│   ├── app.py
│   ├── drift_detector.py
│   └── quality_checker.py
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── jenkins/
│   └── Jenkinsfile
├── docker/
│   ├── Dockerfile
│   └── .dockerignore
├── prometheus/
│   └── prometheus.yml
├── grafana/
│   └── dashboard.json
├── dvc/
│   └── .dvc
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔄 MLOps Workflow

1. **Data Preparation**: Track datasets with DVC
2. **Model Training**: Train and log with MLflow
3. **Containerization**: Build Docker image
4. **CI/CD**: Jenkins pipeline automates build and test
5. **Deployment**: Deploy to Kubernetes
6. **Monitoring**: Track metrics with Prometheus & Grafana
7. **Data Drift**: Detect drift with Evidently AI
8. **Retraining**: Automated retraining on drift detection

## 📊 Monitoring

- **Prometheus**: Access at `http://localhost:9090`
- **Grafana**: Access at `http://localhost:3000`
- **MLflow**: Access at `http://localhost:5001`
- **Streamlit**: Access at `http://localhost:8501`

## 🔧 Configuration

All configurations are managed via:
- `model/config.yaml` - Model hyperparameters
- `prometheus/prometheus.yml` - Metrics scraping
- `k8s/configmap.yaml` - Kubernetes configurations

## 📦 Dependencies

See `requirements.txt` for all Python dependencies.

## 🤝 Contributing

Contributions are welcome! Please follow MLOps best practices.

## 📄 License

MIT License

## 📞 Support

For issues and questions, please open a GitHub issue.

---

**Happy MLOps-ing!** 🚀
