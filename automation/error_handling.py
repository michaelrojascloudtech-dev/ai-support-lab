import requests

url = "https://httpbin.org/delay/5"
payload = {"msg": "testing timeout"}

try:
    response = requests.post(url, json=payload, timeout=3)
    print("Status:", response.status_code)

except requests.exceptions.Timeout:
    print("Timeout: The API did not respond in time.")

