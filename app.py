import streamlit as st
import plotly.express as px
import pandas as pd
import geocoder
import plotly.graph_objects as go

from utils.api import get_aqi
from utils.predictor import classify_aqi, predict_health_risk



st.set_page_config(page_title="Air Quality Health Predictor", layout="wide")

st.title("🌫️ Real-Time Air Quality & Health Risk Predictor")
st.caption("AI-powered system to predict health risk from air pollution")


# ---------------- SIDEBAR ---------------- #

def sidebar_dashboard():
    st.sidebar.title("🌍 Air Quality Dashboard")
    st.sidebar.markdown("📍 Location Detection")
    st.sidebar.write("Click the button to automatically detect your city")
    st.sidebar.markdown("Real-time pollution monitoring system")

    st.sidebar.info("""
    **Project Features**

    • Live AQI Data  
    • Health Risk Detection  
    • Machine Learning Prediction  
    • Pollution Visualization
    """)


# ---------------- METRICS ---------------- #

def display_metrics(city, data):

    st.subheader(f"Air Quality in {city}")

    col1, col2, col3 = st.columns(3)

    col1.metric("AQI", data["aqi"])
    col2.metric("PM2.5", data["pm25"])
    col3.metric("PM10", data["pm10"])

    col1.metric("NO2", data["no2"])
    col2.metric("CO", data["co"])
    col3.metric("Ozone", data["o3"])

    st.markdown("---")
    st.subheader("📊 Air Quality Summary")


# ---------------- HEALTH RISK ---------------- #

def display_health_risk(data):

    risk = classify_aqi(data["aqi"])

    st.subheader(f"Health Risk: {risk}")

    if "Good" in risk:
        st.success("Air quality is good. Outdoor activities are safe")

    elif "Moderate" in risk:
        st.info("Air quality is acceptable, but sensitive people should be cautious")

    elif "Unhealthy for Sensitive Groups" in risk:
        st.warning("Children, elderly, and asthma patients should reduce outdoor activity")

    elif "Unhealthy" in risk:
        st.warning("Avoid outdoor exercise and prolonged exposure")

    elif "Very Unhealthy" in risk:
        st.error("Health alert. Stay indoors if possible")

    else:
        st.error("Serious health risk. Avoid going outside")


# ---------------- ML PREDICTION ---------------- #

def display_ml_prediction(data):

    ml_prediction = predict_health_risk(data)

    st.subheader("🤖 AI Health Risk Prediction")

    st.success(f"Predicted Air Quality Category: {ml_prediction}")


# ---------------- CHART ---------------- #

def display_chart(data):

    pollution_data = {
        "Pollutant": ["AQI", "PM2.5", "PM10", "NO2", "CO", "Ozone"],
        "Value": [
            data["aqi"],
            data["pm25"],
            data["pm10"],
            data["no2"],
            data["co"],
            data["o3"]
        ]
    }

    df = pd.DataFrame(pollution_data)

    fig = px.bar(
        df,
        x="Pollutant",
        y="Value",
        title="Pollutant Levels"
    )

    st.plotly_chart(fig, use_container_width=True)

#-----------------Gauge Chart----------------#
def display_aqi_gauge(data):
    aqi=data["aqi"]
    fig=go.Figure(go.Indicator(
        mode="gauge+number",
        value=aqi,
        title={'text':'AQI Level'},
        gauge={'axis': {'range': [0, 500]},
               'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 50], 'color': "#2ecc71"},
                    {'range': [51, 100], 'color': "#f1c40f"},
                    {'range': [101, 150], 'color': "#e67e22"},
                    {'range': [151, 200], 'color': "#e74c3c"},
                    {'range': [201, 300], 'color': "#8e44ad"},
                    {'range': [301, 500], 'color': "#7f8c8d"}
                ],}
    ))
    st.plotly_chart(fig,use_container_width=True)


# ---------------- MAIN DISPLAY ---------------- #

def show_air_quality(city):

    data = get_aqi(city)

    if data:
        
        display_metrics(city, data)
        display_aqi_gauge(data)
        display_health_risk(data)
        display_ml_prediction(data)
        display_chart(data)
        

    else:
        st.error("City not found or API error.")


# ---------------- LOCATION DETECTION ---------------- #

def detect_location():

    if st.button("📍 Use My Location"):

        g = geocoder.ip('me')

        if g.city:

            city = g.city

            st.success(f"Detected location: {city}")

            show_air_quality(city)

        else:
            st.error("Could not detect your location.")


# ---------------- CITY INPUT FORM ---------------- #

def city_search():

    with st.form("aqi_form"):

        city = st.text_input("Enter City Name", placeholder="e.g., New York")

        submitted = st.form_submit_button("Check Air Quality")

    if submitted:

        if city.strip() == "":
            st.warning("Please enter a city name")

        else:
            show_air_quality(city)


# ---------------- RUN APP ---------------- #

sidebar_dashboard()
detect_location()
city_search()