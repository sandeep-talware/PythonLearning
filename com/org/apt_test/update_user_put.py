import requests

mypayload = {
    "name": "Name_Updated",
    "job": "Updated_Job"
}
resp = requests.put("https://reqres.in/api/users/2",data = mypayload)
print(resp)
print(resp.json())
print(resp.headers.get('Content-Type'))
assert resp.status_code == 200, "Status code is invalid"
print(resp.json()["job"])
assert resp.json()["job"] == "Updated_Job", "Job is incorrect"