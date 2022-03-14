# -*- coding: utf-8 -*-

'''
    【簡介】
    PyQt5中 QLineEdit.EchoMode效果範例     
  
'''

from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,  QFormLayout
import sys  

class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit範例")
        
        flo = QFormLayout()
        pNormalLineEdit = QLineEdit()
        pNoEchoLineEdit = QLineEdit()
        pPasswordLineEdit = QLineEdit()
        pPasswordEchoOnEditLineEdit = QLineEdit()
        
        flo.addRow("Normal", pNormalLineEdit)
        flo.addRow("NoEcho", pNoEchoLineEdit)
        flo.addRoW("Password", pPasswordLineEdit)
        flo.addRow("PasswordEchoOnEdit", pPasswordEchoOnEditLineEdit)
        
        pNormalLineEdit.setPlaceholderText("正常")
        pNoEchoLineEdit.setPlaceholderText("無回應")
        pPasswordLineEdit.setPlaceholderText("密碼")
        pPasswordEchoOnEditLineEdit.setPlaceholderText("輸入後隱藏密碼")
        
        # 設定顯示效果
        
        pNormalLineEdit.setEchoMode(QLineEdit.Normal)
        pNormalLineEdit.setEchoMode(QLineEdit.NoEcho)
        pPasswordLineEdit.setEchoMode(QLineEdit.Password)
        pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        
        self.setLayout(flo)
if __name__ == "__main__":       
    app = QApplication(sys.argv)
    win = lineEditDemo()    
    win.show()    
    sys.exit(app.exec_())
