import requests

resp = requests.get("https://reqres.in/api/users?page=2")
# print(resp)
# print(type(resp))
# print(dir(resp))
code = resp.status_code
assert code == 200, "Status code not correct"
# print(resp.text)
# print(resp.content)
print(resp.json())
print(type(resp.headers))
print(resp.headers)
print(type(resp.cookies))
print(resp.cookies)
print(resp.encoding)
print(resp.url)