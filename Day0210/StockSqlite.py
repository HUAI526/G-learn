# -*- coding:utf-8 -*-
import sqlite3
import requests
import datetime
conn = sqlite3.connect('stock.sqlite')

sqlstr = ''' CREATE TABLE "stock" \
(
"證券代號" TEXT PRIMARY KEY NOT NULL,
"證券名稱" TEXT NOT NULL,
"成交股數" TEXT NOT NULL,
"成交筆數" TEXT NOT NULL,
"成交金額" TEXT NOT NULL,
"開盤價" TEXT NOT NULL,
"最高價" TEXT NOT NULL,
"最低價" TEXT NOT NULL,
"收盤價" TEXT NOT NULL,
"漲跌" TEXT NOT NULL,
"漲跌價差" TEXT NOT NULL,
"最後揭示買價" TEXT NOT NULL,
"最後揭示買量" TEXT NOT NULL,
"最後揭示賣價" TEXT NOT NULL,
"最後揭示賣量" TEXT NOT NULL,
"本益比" TEXT NOT NULL
)
'''
conn.execute(sqlstr)

now = datetime.datetime.now()
url ='https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date='+\
    (now-datetime.timedelta(hours = 20)).strftime('%Y%m%d') + '&type=ALL'
res = requests.get(url)
dataText = res.text
sep = '"證券代號","證券名稱","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","漲跌價差","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比",'
dataText = dataText.split(sep)[1]
dataText = dataText.replace('\r','')
dataText = dataText.split('\n')

for dataString in dataText:
    if len(dataString)>0 and not dataString[0] == '=':
        dataString2 = dataString.replace('","', '&')
        dataString2 = dataString2.replace(',', '')
        dataString2 = dataString2.replace('&', '","')
        sqlstr = '''INSERT INTO stock (證券代號,證券名稱,成交股數,成交筆數,成交金額,開盤價,最高價,最低價,收盤價,漲跌,漲跌價差,最後揭示買價,最後揭示買量,最後揭示賣價,最後揭示賣量,本益比) VALUES
            (
            '''
        sqlstr=sqlstr+dataString2+')'
        conn.execute(sqlstr)

conn.commit()
conn.colse()