import joblib
import pandas as pd
model=joblib.load("models/aqi_model.pkl")

def classify_aqi(aqi):
    if aqi<=50:
        return "Good 🟢"
    elif aqi<=100:
        return "Moderate 🟡"
    elif aqi<=150:
        return "Unhealthy for Sensitive Groups 🟠"
    elif aqi<=200:
        return "Unhealthy 🔴"
    elif aqi<=300:
        return "Very Unhealthy 🟣"
    else:
        return "Hazardous ⚠️"
    
def predict_health_risk(data):
    input_data=pd.DataFrame([[
        data["aqi"],
        data["co"],
        data["o3"],
        data["no2"],
        data["pm25"]
    ]],
    columns=[
        "AQI Value",
        "CO AQI Value",
        "Ozone AQI Value",
        "NO2 AQI Value",
        "PM2.5 AQI Value"
    ])
    prediction=model.predict(input_data)
    return prediction[0]