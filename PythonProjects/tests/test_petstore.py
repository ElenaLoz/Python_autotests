import requests
import pytest

def test_statuscod():
    response = requests.get("https://petstore.swagger.io/v2/pet/3")
    assert response.status_code == 200

def test_1():
    response = requests.get("https://petstore.swagger.io/v2/pet/3")
    assert response.json()["name"] == "doggieSS"