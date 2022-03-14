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
    dataDic1={}
with open('StockData.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    
    for row in rows:
        
    
print(row)