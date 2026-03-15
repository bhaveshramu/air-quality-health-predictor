from utils.api import get_aqi

city = "Bangalore"

data = get_aqi(city)

print(data)