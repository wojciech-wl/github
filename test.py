import requests

API_KEY = "your_api_key"
CITY = "Warsaw"
url = f"..."

response = requests.get(url)
data = response.json()

temp = data['current']['temp_c']
condition = data['current']['condition']['text']

print(f"{CITY}: {temp}°C, {condition}")
