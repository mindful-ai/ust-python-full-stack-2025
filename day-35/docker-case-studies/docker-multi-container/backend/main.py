from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

MODEL_SERVING_URL = "http://model_serving:5001/predict"

# Define expected request body
class FeaturesRequest(BaseModel):
    features: list[float]

@app.post("/predict")
async def get_prediction(request: FeaturesRequest):
    try:
        response = requests.post(MODEL_SERVING_URL, json={"features": request.features})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
