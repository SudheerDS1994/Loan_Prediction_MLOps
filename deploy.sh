#!/bin/bash

# Script to deploy to Kubernetes

echo "====================================="
echo "Kubernetes Deployment Script"
echo "====================================="

# Check kubectl
echo "Checking kubectl..."
kubectl version --client

# Create namespace
echo "Creating namespace..."
kubectl create namespace mlops || true

# Apply configurations
echo "Applying Kubernetes configurations..."
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Check deployment status
echo "Checking deployment status..."
kubectl get deployments
kubectl get pods
kubectl get svc

echo ""
echo "Deployment completed!"
