import requests
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et
def getData():
    dataDic1={}
    user_key = "CWB-D6430C07-0E89-4E27-A0F7-1D97F7C9C469"
    doc_name = "F-C0032-001"

    api_link = "https://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s"\
        % (doc_name,user_key)
    
    report = requests.get(api_link).text
    #print(report)

    xml_namespace = "{urn:cwb:gov:tw:cwbcommon:0.1}"
    root = et.fromstring(report)
    dataset = root.find(xml_namespace + "dataset")
    locations_info = dataset.findall(xml_namespace + 'location')

    for idx,ele in enumerate(locations_info):
        locationName = ele[0].text
        print(locationName)
        show = ''
        dataArr=[]
        tlist = ['天氣狀況', '最高溫', '最低溫', '舒適度','降雨機率']
    
        for i in range(5):
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
        
        self.p1.setReadOnly(True)
        self.p2.setReadOnly(True)
        self.p3.setReadOnly(True)
        self.p4.setReadOnly(True)
        self.p5.setReadOnly(True)
        flo.addRow("天氣狀況",self.p1)
        flo.addRow("最高溫",self.p2)
        flo.addRow("最低溫",self.p3)
        flo.addRow("舒適度",self.p4)
        flo.addRow("降雨機率",self.p5)
        layout.addLayout(flo)
        self.setLayout(layout)
        self.setWindowTitle("氣象局今明預報")
    def clicked(self,item):
        self.p1.setText(str(self.dataDic1[item.text()][0]))
        self.p2.setText(str(self.dataDic1[item.text()][1]))
        self.p3.setText(str(self.dataDic1[item.text()][2]))
        self.p4.setText(str(self.dataDic1[item.text()][3]))
        self.p5.setText(str(self.dataDic1[item.text()][4]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = cwb()
    demo.show()
    sys.exit(app.exec_())