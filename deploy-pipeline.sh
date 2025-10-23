#!/bin/bash

echo "Starting CI/CD Pipeline..."

echo "Building Docker image..."
docker build -t whalesnail/my-custom-app:latest .

echo "Pushing to Docker Hub..."
docker push whalesnail/my-custom-app:latest

echo "Deploying to Kubernetes..."
kubectl rollout restart deployment/my-app

echo "Waiting for rollout to complete..."
kubectl rollout status deployment/my-app

echo "Pipeline complete! Your app is deployed!"

