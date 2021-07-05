import requests

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
resp = requests.post(url="https://reqres.in/api/register",data=payload)
print(resp)
print(resp.json())
print(resp.json()['token'])
assert resp.json()['token'] != None,"Token connot be non"