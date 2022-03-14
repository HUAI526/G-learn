# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime
import requests
import csv
from bs4 import BeautifulSoup

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

def getData():    

    with open('StockData.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            dict(row["證券代號"],row["證券名稱"],row["成交股數"],row["成交筆數"],row["成交金額"],row["開盤價"],row["最高價"],row["最低價"],row["收盤價"],row["漲跌(+/-)"],row["本益比"])
    

    dataDic1={}
    
    root = et.fromstring(save())
    stock_Number = root.find("證券代號")
    

    for idx,ele in enumerate(locations_info):
        locationName = ele[0].text
        print(locationName)
        show = ''
        dataArr=[]
        tlist = ["證券代號","證券名稱","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","本益比"]
    
        for i in range(11):
            element = locations_info[idx][i+1]
            timeblock = element[1]
            data = timeblock[2][0].text
            show = show + tlist[i] + ':' + data + data +'\n'
            dataArr.append(data)
        print(show)
        dataDic1[str(locationName)]=dataArr
    return dataDic1


class cwb(QWidget):
    def __init__(self):
        super().__init__()
        self.dataDic1=getData()
        layout = QHBoxLayout()
        ListWidget = QListWidget()
        for item in self.dataDic1.keys():
            ListWidget.addItem(str(item))
        ListWidget.itemClicked.connect(self.clicked)
        layout.addWidget(ListWidget)
        
        flo = QFormLayout()
        self.p1 = QLineEdit()
        self.p2 = QLineEdit()
        self.p3 = QLineEdit()
        self.p4 = QLineEdit()
        self.p5 = QLineEdit()
        self.p6 = QLineEdit()
        self.p7 = QLineEdit()
        self.p8 = QLineEdit()
        
        self.p1.setReadOnly(True)
        self.p2.setReadOnly(True)
        self.p3.setReadOnly(True)
        self.p4.setReadOnly(True)
        self.p5.setReadOnly(True)
        self.p6.setReadOnly(True)
        self.p7.setReadOnly(True)
        self.p8.setReadOnly(True)
        flo.addRow("成交股數",self.p0)
        flo.addRow("成交筆數",self.p1)
        flo.addRow("成交金額",self.p2)
        flo.addRow("開盤價",self.p3)
        flo.addRow("最高價",self.p4)
        flo.addRow("最低價",self.p5)
        flo.addRow("收盤價",self.p6)
        flo.addRow("本益比",self.p7)
        layout.addLayout(flo)
        self.setLayout(layout)
        self.setWindowTitle("股票")
    def clicked(self,item):
        self.p0.setText(str(self.dataDic1[item.text()][0]))
        self.p1.setText(str(self.dataDic1[item.text()][1]))
        self.p2.setText(str(self.dataDic1[item.text()][2]))
        self.p3.setText(str(self.dataDic1[item.text()][3]))
        self.p4.setText(str(self.dataDic1[item.text()][4]))
        self.p5.setText(str(self.dataDic1[item.text()][5]))
        self.p6.setText(str(self.dataDic1[item.text()][6]))
        self.p7.setText(str(self.dataDic1[item.text()][7]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = cwb()
    demo.show()
    sys.exit(app.exec_())