# 💳 Loan Approval Prediction System

## 🚀 Overview
This project is a production-ready Machine Learning system that predicts whether a loan application should be approved based on applicant details.

It includes:
- Data preprocessing pipeline
- Feature engineering
- XGBoost model training
- FastAPI backend for real-time predictions

---

## 📊 Features Used
- Gender
- Married
- Dependents
- Education
- Self_Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Property_Area

---

## 🧠 ML Pipeline
1. Data Cleaning (handling missing values)
2. Feature Engineering (income ratios)
3. One-hot encoding
4. Model Training using XGBoost
5. Saving model + feature columns

---

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- FastAPI

---

## 🧪 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

Train model
python src/train.py

Run API
uvicorn api.app:app --reload
Dtaset
###https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset
