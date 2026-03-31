import requests

login_url = "http://localhost:8000/api/v1/login/access-token"

data = {"username": "admin@example.com", "password": "admin123"}

response = requests.post(login_url, data=data)


print(response.json())

token = response.json()["access_token"]

url = "http://localhost:8000/api/v1/items/"

headers = {"Authorization": f"Bearer {token}"}

data = {"title": "hello", "description": "world"}

response = requests.post(url, json=data, headers=headers)

print(response.status_code, response.json())
