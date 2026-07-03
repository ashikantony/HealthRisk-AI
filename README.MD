# HealthRisk AI

## Overview
HealthRisk AI is a dual-domain artificial intelligence platform that integrates healthcare intelligence and financial risk analytics.

The system combines:

- Clinical Outcome Prediction
- Epidemiological Modelling
- Patient Risk Stratification
- Pharmaceutical Efficacy Analysis
- Insurance Actuarial Modelling
- Hospital Credit Risk Scoring
- Pharmaceutical Portfolio Optimization
- Health-Sector ESG Analytics
- HealthRisk Lab Gamified Simulation Platform

---

## Repository Structure

healthrisk-ai
├── .github/
├── configs/
├── data/
├── models/
├── simulation/
├── explainability/
├── notebooks/
├── docs/
├── reports/
└── tests/

---

## Technology Stack

### Backend
- Python 3.11
- FastAPI
- PostgreSQL

### Machine Learning
- Scikit-Learn
- XGBoost
- LightGBM
- TensorFlow
- PyTorch

### Visualization
- Streamlit
- Plotly
- Matplotlib

### Explainability
- SHAP
- LIME

### Containerization
- Docker
- Docker Compose

---

## Installation

### Clone Repository

git clone https://github.com/yourusername/healthrisk-ai.git

cd healthrisk-ai

### Create Environment

python -m venv venv

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

---

## Run Application

docker-compose up --build

or

streamlit run simulation/game_engine.py


MIT License
