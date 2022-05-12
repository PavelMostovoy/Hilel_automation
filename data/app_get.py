import requests

url = "https://www.aqa.science/users/"
url_post = "https://www.aqa.science/users/14/"

data = {
    "username": "Post_user",
    "email": "post@user.data",
    "groups": []
}

user = "admin"
password = "admin123"

# resp_post = requests.post(url, data, auth=(user, password))

# resp = requests.get(url_post, auth=(user, password)).json()

# print(resp_post.json())
