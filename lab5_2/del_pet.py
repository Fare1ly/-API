import pytest
import requests


class Test_pet:
    def test_create_pet(self):
        json = {
            "id": 7777,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "kitty",
            "photoUrls": [
                "string"
                ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        response = requests.post("https://petstore.swagger.io/v2/pet", json=json)
        assert response.status_code == 200
        assert response.json()["name"] == "kitty"
        assert response.json()["id"] == 7777

    def test_del_pet(self):
        response = requests.delete("https://petstore.swagger.io/v2/pet/7777")
        assert response.status_code == 200
        assert response.json()["type"] == "unknown"
        assert response.json()["message"] == "7777"