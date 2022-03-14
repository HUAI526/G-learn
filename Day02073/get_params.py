import requests
payload = {'key1':'valuel', 'key2':'value2'}

r = requests.get("https://httpbin.org/get", params=payload)
print(r.text)