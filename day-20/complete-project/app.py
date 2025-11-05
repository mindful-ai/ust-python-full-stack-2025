# fastapi_app.py
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

# Load model
with open("artifacts/heart_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI(title="Heart Disease Prediction API")

# Input schema
class HeartData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int


@app.post("/predict")
def predict(data: HeartData):
    # Feature names used during model training
    feature_names = [
        "age", "sex", "cp", "trestbps", "chol",
        "fbs", "restecg", "thalach", "exang",
        "oldpeak", "slope", "ca", "thal"
    ]

    # Convert input into DataFrame
    features = pd.DataFrame([[
        data.age, data.sex, data.cp, data.trestbps, data.chol,
        data.fbs, data.restecg, data.thalach, data.exang,
        data.oldpeak, data.slope, data.ca, data.thal
    ]], columns=feature_names)

    # Prediction
    prediction = model.predict(features)[0]

    # Probability (if model supports it)
    try:
        probability = float(model.predict_proba(features)[0][1])
    except AttributeError:
        probability = None

    result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

    return {
        "prediction": int(prediction),
        "result": result,
        "probability": probability
    }
