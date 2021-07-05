import requests

resp = requests.delete(url="https://reqres.in/api/users/2")
print(resp)
assert resp.status_code == 204, "User deletion failed"