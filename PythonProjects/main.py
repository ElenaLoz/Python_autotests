import requests
import pytest
url = "https://petstore.swagger.io/v2/pet"
response = requests.post (url, json= {
    "id": 3,
  "category": {
    "id": 3,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 3,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response = requests.put (url, json= {
    "id": 3,
  "category": {
    "id": 3,
    "name": "string"
  },
  "name": "doggieSS",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 3,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

url = "https://petstore.swagger.io/v2/pet/3"
response = requests.get (url)
print(response.text)