import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class qtApp(QWidget) :
    def __init__(self) :
        super().__init__()
        uic.loadUi('./studyPyQt/calculator.ui',self)
        # self.setWindowIcon(QIcon('./studyPyQt/addressbook.png'))
        # self.setWindowTitle('주소록 v0.5')

        # 시그널 16개에 슬롯함수는 1개
        self.btn_C.clicked.connect(self.btnClicked)
        self.btn_number0.clicked.connect(self.btnClicked)
        self.btn_number1.clicked.connect(self.btnClicked)
        self.btn_number2.clicked.connect(self.btnClicked)
        self.btn_number3.clicked.connect(self.btnClicked)
        self.btn_number4.clicked.connect(self.btnClicked)
        self.btn_number5.clicked.connect(self.btnClicked)
        self.btn_number6.clicked.connect(self.btnClicked)
        self.btn_number7.clicked.connect(self.btnClicked)
        self.btn_number8.clicked.connect(self.btnClicked)
        self.btn_number9.clicked.connect(self.btnClicked)
        self.btn_result.clicked.connect(self.btnClicked)
        self.btn_add.clicked.connect(self.btnClicked)
        self.btn_minus.clicked.connect(self.btnClicked)
        self.btn_multipy.clicked.connect(self.btnClicked)
        self.btn_divide.clicked.connect(self.btnClicked)
        
        self.txt_view.setEnabled(False)
        self.txt_value = ''
    
    def btnClicked(self) :
        btn_val = self.sender().text()
        if btn_val == 'C' : # Clear
            print("clear")
            self.txt_view.setText('0')
            self.txt_value = ''
        elif btn_val == '=' :
            print('=')
            try :
                result = eval(self.txt_value.lstrip('0'))
                result = round(result,4)
                print(result)
                self.txt_view.setText(str(result))
            except :
                self.txt_view.setText('ERROR')
        else :
            if btn_val == 'X' :
                btn_val = '*'
            self.txt_value += btn_val
            print(self.txt_value)
            self.txt_view.setText(self.txt_value)


if __name__ == '__main__' :    
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())