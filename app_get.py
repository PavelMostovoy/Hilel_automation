import requests
import json
import logging
logging.basicConfig(filename='logs/example.log', level=logging.DEBUG)
LOGGER = logging.getLogger("main")


file_name = "variables.json"
resources_folder = "resources"

# resources/variables.json

with open(f"./{resources_folder}/{file_name}", "r") as f:
    variables = json.load(f)


data = {
    "username": "Bill",
    "email": "examole@example.com",
    "groups": []
}

# for user, password in variables["users"].items():
#     resp = requests.get(variables['urls']['main']).json()
#     break

user = "admin"
password = variables["users"][user]
url = f"{variables['urls']['main']}{variables['urls']['users']}"

resp = requests.get(url, auth=(user, password))
LOGGER.info(resp.json())

assert resp.status_code == 200, resp.status_code

resp_data = resp.json()

url_user = f"{url}44"

resp = requests.get(url_user, auth=(user, password))

LOGGER.info(f"{url_user}  :  {resp.json()}")


resp_post = requests.post(url, data, auth=(user, password))


assert resp_post.status_code == 201, LOGGER.error(resp_post.content)

