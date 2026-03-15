import requests

API_TOKEN = "9852ece41bed1713289d7a1adfa84732d99f75ba"

def get_aqi(city):
    
    url = f"https://api.waqi.info/feed/{city}/?token={API_TOKEN}"
    
    response = requests.get(url)
    data = response.json()
    
    if data["status"] == "ok":
        aqi = data["data"]["aqi"]
        pollutants = data["data"]["iaqi"]
        
        result = {
            "aqi": aqi,
            "pm25": pollutants.get("pm25", {}).get("v", None),
            "pm10": pollutants.get("pm10", {}).get("v", None),
            "no2": pollutants.get("no2", {}).get("v", None),
            "co": pollutants.get("co", {}).get("v", None),
            "o3": pollutants.get("o3", {}).get("v", None),
        }
        
        return result
    
    return None