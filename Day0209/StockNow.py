# -*- coding: utf-8 -*-
import datetime
import requests


from bs4 import BeautifulSoup

def getStockIds():
    now = datetime.datetime.now()
    url ='https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date='+\
        (now-datetime.timedelta(hours = 20)).strftime('%Y%m%d') + '&type=ALL'
    res = requests.get(url)
    dataText = res.text
    sep = '"證券代號","證券名稱","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","漲跌價差","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比"'
    dataText = dataText.split(sep)[1]
    dataText = dataText.replace('\r','')
    dataText = dataText.split('\n')
    result = sep+'\n'
    for dataString in dataText:
        if len(dataString)>0 and not dataString[0] == '=':
            result = result + '=' + dataString  + '\n'
            
    
    print(result)
    
    dataFile = open('StockData.csv', 'w')
    dataFile.write(result)
    
if __name__ == '__main__':
    getStockIds()
    