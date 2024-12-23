import requests


def get_token_auth():
    url = "___"
    data = {"username": "___", "password": "____"}
    response = requests.post(url, json=data)
    return response.json()["token"]