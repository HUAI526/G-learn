# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication


#1

class Icon(QWidget):
    def __init__(self, parent=None):
        super(Icon,self).__init__(parent)
        self.initUI()
        
        def initUI(self):
            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle("展示城市圖範例")
            self.setWindowIcon(QIcon('./images/cartoonl.ico'))
            
if __name__=='__main__':
    app = QApplication(sys.argv)
    icon = Icon()
    icon.show()
    sys.exit(app.exec_()) 