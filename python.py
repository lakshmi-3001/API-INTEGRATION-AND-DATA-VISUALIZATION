import json
import requests

city_name= input("what is your city name?")

api_key="894b3438ccd4581748883cfd2bcff3b4"

api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

response = requests.get(api_url)
data = response.json()
simplified_data =json.dumps(data, indent=4)
print(simplified_data)

print(data)

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

labels = ['Temperature', 'Feels Like', 'Humidity']
values = [data['main']['temp'], data['main']['feels_like'], data['main']['humidity']]

plt.figure(figsize=(8, 5))
plt.bar(labels, values, color=['yellow', 'orange', 'green'])
plt.title(f"Current Weather in {data['name']}")
plt.ylabel("Value")
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

cloud_coverage = data['clouds']['all']
clear = 100 - cloud_coverage

plt.figure(figsize=(6, 6))
plt.pie([clear, cloud_coverage], labels=['Clear', 'Cloudy'], autopct='%1.1f%%', colors=['lightblue', 'gray'])
plt.title("Cloud Cover")
plt.show()

wind_speed = data['wind']['speed']
print(f"Wind Speed: {wind_speed} m/s")
