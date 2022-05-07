import requests



response = requests.get("https://wikipedia.com/json")

print(response.json)
