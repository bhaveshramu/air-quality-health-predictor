import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# load dataset
data = pd.read_csv("data/air_quality_dataset.csv")

# features (input data)
X = data[[
    "AQI Value",
    "CO AQI Value",
    "Ozone AQI Value",
    "NO2 AQI Value",
    "PM2.5 AQI Value"
]]

# target (prediction)
y = data["AQI Category"]

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model
model = RandomForestClassifier(n_estimators=100)

model.fit(X_train, y_train)

# predictions
pred = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, pred))

# save model
joblib.dump(model, "models/aqi_model.pkl")