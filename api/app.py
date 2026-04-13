from fastapi import FastAPI
import joblib
import pandas as pd

from src.preprocessing import preprocess
from src.feature_engineering import create_features

app = FastAPI()

model = joblib.load("models/model.pkl")
columns = joblib.load("models/columns.pkl")


@app.get("/")
def home():
    return {"message": "Loan Approval API Running"}


@app.post("/predict")
def predict(data: dict):
    try:
        # Convert input to DataFrame
        df = pd.DataFrame([data])

        # Apply same preprocessing
        df = preprocess(df)
        df = create_features(df)

        # One-hot encoding
        df = pd.get_dummies(df)

        # Align columns with training
        df = df.reindex(columns=columns, fill_value=0)

        # Prediction
        prediction = model.predict(df)

        return {"Loan Approved": bool(prediction[0])}

    except Exception as e:
        return {"error": str(e)}