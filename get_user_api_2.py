import requests

query_param = {"page":2}
resp = requests.get(url="https://reqres.in/api/users",params=query_param)
# print(resp)
# print(type(resp))
# print(dir(resp))
code = resp.status_code
assert code == 200, "Status code not correct"
# print(resp.text)
# print(resp.content)
print(resp.url)
json_respose = resp.json()
print(json_respose['total'])
assert json_respose['total'] == 12, "Total count is not matching"
print(json_respose['total_pages'])
assert json_respose['total_pages'] == 2, "Total Pages count is not matching"
print(json_respose["data"][0]["email"])
assert (json_respose["data"][0]["email"]).endswith("reqres.in"),"mail id is not matching"
print(json_respose["data"][1]["first_name"])
assert (json_respose["data"][1]["first_name"]) == "Lindsay" ,"first name is not matching"
print(json_respose["data"][2]["last_name"])
assert json_respose["data"][2]["last_name"] != None,"last name is matching"

print(json_respose["support"]["url"])
assert (json_respose["support"]["url"]).endswith("https"), "Not valid URL"