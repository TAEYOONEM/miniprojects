import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class qtApp(QMainWindow) :
    def __init__(self) :
        super().__init__()
        uic.loadUi('./studyThread/threadApp.ui',self)
        self.setWindowTitle('NO THREAD APP v0.4')
        self.pgbTask.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)

    def btnStartClicked(self) :
        self.pgbTask.setRange(0,999999) 
        for i in range(0,1000000) : 
            print(f'Print No Thread > {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'Print No Thread > {i}')


if __name__ == '__main__' :    
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())