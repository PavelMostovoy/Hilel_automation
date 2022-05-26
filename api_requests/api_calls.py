"""
File with explanation for API
"""
import json

import requests

URL = "https://www.aqa.science"
USER = "admin"
PASSWORD = "admin123"

first_response = requests.get(URL).json()

results = []


def get_user_list(users_url):
    global results
    response = requests.get(users_url, auth=(USER, PASSWORD))
    initial_object = response.json()
    results += initial_object["results"]
    next_ = initial_object["next"]
    if next_:
        get_user_list(next_)


get_user_list("https://www.aqa.science/users")

print(len(results))

with open("response.json", "w") as f:
    json.dump(results, f)


