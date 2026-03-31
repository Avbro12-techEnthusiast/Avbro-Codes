import requests
import matplotlib.pyplot as plt

print("*****WELCOME TO AQI MONITORING SYSTEMS*****")

cities = input("Enter the names of cities separated by comma: ").split(",")

api_key = "3bcbcd38eb096ff9c35e6e256104a4f8a84dea3b"

city_names = []
aqi_values = []

for city in cities:

    city = city.strip()

    url = f"https://api.waqi.info/feed/{city}/?token={api_key}"

    response = requests.get(url)
    data = response.json()

    try:
        aqi = data["data"]["aqi"]

        print(city, "AQI:", aqi)

        city_names.append(city)
        aqi_values.append(aqi)

    except:
        print(city, "AQI data not available")

plt.bar(city_names, aqi_values)

plt.title("AQI Comparison Between Cities")
plt.xlabel("Cities")
plt.ylabel("AQI")

plt.show()