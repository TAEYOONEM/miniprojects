# Qt Designer 디자인 사용
import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

class qtApp(QWidget) :
    cnt = 0 # 클릭횟수 카운트 변수
    
    def __init__(self) :
        super().__init__()
        uic.loadUi('./studyPyQt/mainApp.ui',self)

        # Qt Designer에서 구성한 위젯시그널 만듬
        self.btnOk.clicked.connect(self.btnOkClicked)
        self.btnPop.clicked.connect(self.btnPopClicked)
    
    def btnOkClicked(self) : # 슬롯함수
        self.cnt += 1
        self.lblMessage.clear()
        self.lblMessage.setText(f'메시지: ok!! + {self.cnt}')
        
    def btnPopClicked(self) :
        QMessageBox.about(self,"popup","kkk")    

if __name__ == '__main__' :    
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())