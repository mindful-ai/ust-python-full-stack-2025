# streamlit_app.py
import streamlit as st
import requests
import logging

# Configure logging
logging.basicConfig(
    filename="frontend.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="centered")

st.title("❤️ Heart Disease Prediction (FastAPI + Streamlit + Logging)")
st.markdown("Enter your medical parameters below and click **Predict** to check your heart health status.")

# Input fields
age = st.number_input("Age", 20, 100, 50)
sex = st.selectbox("Sex (1=Male, 0=Female)", [0, 1])
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.number_input("Serum Cholestoral (mg/dl)", 100, 400, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)", [0, 1])
restecg = st.selectbox("Resting ECG (0–2)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina (1=Yes, 0=No)", [0, 1])
oldpeak = st.number_input("ST Depression", 0.0, 10.0, 1.0, step=0.1)
slope = st.selectbox("Slope of ST Segment (0–2)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (1=Normal, 2=Fixed, 3=Reversible)", [1, 2, 3])

API_URL = "http://127.0.0.1:8000/predict"

if st.button("🚀 Predict"):
    input_data = {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps,
        "chol": chol, "fbs": fbs, "restecg": restecg, "thalach": thalach,
        "exang": exang, "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
    }

    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()
            probability = result.get("probability")

            if probability is not None:
                st.success(f"✅ {result['result']} — Probability: **{probability:.2f}**")
            else:
                st.success(f"✅ {result['result']}")

            logging.info(f"User input: {input_data} -> Result: {result}")
        else:
            st.error("❌ API error. Check backend logs.")
            logging.error(f"API Error: {response.text}")

    except Exception as e:
        st.error(f"⚠️ Error connecting to API: {e}")
        logging.error("Frontend Error", exc_info=True)
