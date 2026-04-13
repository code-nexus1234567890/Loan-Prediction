import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

from preprocessing import preprocess
from feature_engineering import create_features

# Load data
df = pd.read_csv("data/raw/train.csv")

# Preprocess
df = preprocess(df)

# Feature engineering
df = create_features(df)

# Encoding
df = pd.get_dummies(df, drop_first=True)

# Split
X = df.drop("Loan_Status_Y", axis=1)
y = df["Loan_Status_Y"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = XGBClassifier(n_estimators=200, max_depth=5)
model.fit(X_train, y_train)

# ✅ Save BOTH properly (order matters) 
joblib.dump(X.columns.tolist(), "models/columns.pkl")
joblib.dump(model, "models/model.pkl")

print("✅ Model + columns saved successfully")