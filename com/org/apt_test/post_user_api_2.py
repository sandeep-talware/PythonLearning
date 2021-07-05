import json
import requests

resp = requests.post(url="https://reqres.in/api/users",data=json.load(open("create_data.json","r")))
print(resp)
print(resp.json())
assert resp.json()['job'] == 'Development Engineer', "Job is mismatching"