import requests
from bs4 import BeautifulSoup

url = 'https://www.taiwanlottery.com.tw/result_all.htm'
r = requests.get(url)
r.encoding = 'UTF-8'
sp = BeautifulSoup(r.text, 'html.parser')

#找到威力彩的區塊
datas = sp.find('div', class_='intx01')
datas = datas.find('ul', class_='txin')
#print(datas)

#找到開講期數
datas = datas.find_all('td', class_='even')
title = datas[1].find('span', id='SL638DrawTerm_new').text
#print('威力彩期數:', title)

#找到開獎號碼
nums = datas[4].find_all('span')
#print(nums)

#開出順序
print('大小順序:', end=' ')
for i in range(0,6):
    print(nums[i].text, end='')
#開出順序
print('\n開出順序:', end=' ')
for i in range(7,13):
    print(nums[i].text, end=' ')
    
#第二區
print('\n第二區', end=' ')
print(nums[6].text, end=' ')