import requests

api_address = "https://api.openweathermap.org/data/2.5/weather?lat=12.97&lon=77.59&appid="


json_data = requests.get(api_address).json()
print(json_data)
def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    descriptions = json_data["weather"][0]["description"]
    return descriptions

print(temp())
print(des())