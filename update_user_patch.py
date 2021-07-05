import requests

mypayload = {
    "name": "Name_Updated",
    "job":"job_updated"
}
resp = requests.patch("https://reqres.in/api/users/110",data = mypayload)
print(resp)
print(resp.json())
print(resp.headers.get('Content-Type'))
assert resp.status_code == 200, "Status code is invalid"
print(resp.json()["job"])
assert resp.json()["job"] == "job_updated", "Job is incorrect"