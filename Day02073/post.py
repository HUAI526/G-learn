import requests
payload = {'key1':'value1','key1':'value2'}
r = requests.post("https://httpbin.org/post", data=payload)

print(r.text)