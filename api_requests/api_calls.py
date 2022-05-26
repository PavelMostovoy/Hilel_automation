"""
File with explanation for API
"""
import json

import requests

URL = "https://www.aqa.science"
USER = "admin"
PASSWORD = "admin123"


first_response = requests.get(URL).json()

for item in first_response.values():
    second_response = requests.get(item, auth=(USER, PASSWORD))
    with open("response.json", "w") as f:
        json.dump(second_response.json(), f)

    # break for first item
    break
    # print(second_response.status_code)
    # print(second_response.json())
