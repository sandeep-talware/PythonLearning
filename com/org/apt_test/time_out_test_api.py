import requests

try:
    resp = requests.get(url="https://httpbin.org/delay/5",timeout=5)
    print(resp.status_code)
except requests.exceptions.ReadTimeout:
    print("Timeout Exception")
finally:
    print("done")