import requests

url = "https://httpbin.org/post"
payload = {"text": "Hello API"}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response body:", response.text)