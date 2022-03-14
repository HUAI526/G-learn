import requests
url = 'https://www.twse.com.tw/zh/'
r = requests.get(url)

if r.status_code == requests.codes.ok:
    print(r.text) 