# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QApplication
from PyQt5.QtGui import QFont

class Winform(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('這是一個<b>氣泡提示<b>')
        self.setWindowTitle('氣泡提示DEMO')
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec()) 