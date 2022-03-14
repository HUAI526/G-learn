import requests
url = 'https://www.twse.com.tw/zh/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }

r = requests.get(url, headers=headers)
print(r)