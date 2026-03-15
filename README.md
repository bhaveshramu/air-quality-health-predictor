# 🌫️ Real-Time Air Quality & Health Risk Predictor

An AI-powered web application that analyzes real-time air pollution data and predicts health risks using machine learning.
The system fetches live air quality data for any city, analyzes pollutant levels, and provides personalized health risk insights through an interactive dashboard.

---

## 📌 Project Overview

Air pollution has become one of the most critical environmental and public health challenges worldwide. Most existing applications only show Air Quality Index (AQI) values without explaining what those numbers mean for human health.

This project solves that problem by combining:

* 🌍 Real-time AQI data from APIs
* 🤖 Machine Learning-based risk prediction
* 📊 Interactive data visualization
* 🧑‍⚕️ Health risk interpretation

The application provides an easy-to-understand dashboard that helps users understand pollution levels and potential health risks.

---

## 🚀 Features

* 🌍 Real-time air quality data for any city
* 📍 Automatic location detection
* 📊 Interactive pollution charts
* 🌡️ AQI gauge visualization
* ⚠️ Health risk classification based on AQI
* 🤖 Machine learning prediction for air quality category
* 🖥️ Modern Streamlit dashboard UI

---

## 🧠 Machine Learning Model

The project uses a **Random Forest Classifier** to predict air quality categories based on pollutant values.

### Model Inputs

* AQI Value
* PM2.5
* PM10
* NO₂
* CO
* Ozone

### Model Output

* Air Quality Category Prediction

Example predictions include:

* Good
* Moderate
* Unhealthy
* Very Unhealthy
* Hazardous

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* Streamlit
* Pandas
* Scikit-learn
* Plotly
* Requests
* Geocoder

### APIs

* WAQI (World Air Quality Index API)

### Tools

* Git
* GitHub
* Kaggle Dataset

---

## 📂 Project Structure

```
air-quality-health-predictor
│
├── app.py
├── train_model.py
├── requirements.txt
│
├── utils
│   ├── api.py
│   └── predictor.py
│
├── models
│   └── aqi_model.pkl
│
├── data
│   └── air_quality_dataset.csv
│
└── README.md
```

---

## ⚙️ Installation & Setup

1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/air-quality-health-predictor.git
```

2️⃣ Navigate to the project folder

```
cd air-quality-health-predictor
```

3️⃣ Install dependencies

```
pip install -r requirements.txt
```

4️⃣ Run the Streamlit app

```
streamlit run app.py
```

The dashboard will open in your browser.

---

## 📊 Dashboard Features

The application dashboard provides:

* Real-time AQI metrics
* Pollution level visualization
* AQI gauge indicator
* Health risk analysis
* AI-based air quality prediction

Users can either:

* Enter a city name manually
* Use automatic location detection

---

## 🔮 Future Improvements

Possible extensions for this project include:

* 7-day AQI forecasting using time-series models
* Mobile app version
* Integration with IoT pollution sensors
* Personalized health recommendations
* Smart city environmental monitoring system

---

## 📜 License

This project is open-source and available for educational purposes.
