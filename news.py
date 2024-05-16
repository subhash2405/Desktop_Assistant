import requests

api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey="
json_data = requests.get(api_address).json()

arr = []
def news():
    for i in range(5):
        arr.append(json_data["articles"][i]["title"]+".")
    return arr

