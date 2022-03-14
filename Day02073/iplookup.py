import requests

url = 'https://api.ipify.org'
r = requests.get(url)

print('我目前的IP位置是:', r.text)