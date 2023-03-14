import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

class BackgroungWorker(QThread) : # PyQt5 스레드를 위한 클래스 존재
    procChanged = pyqtSignal(str)

    def __init__(self,count = 0 ,parent = None) -> None:
        super().__init__()
        self.main = parent
        self.working = True # 스레드 동작여부
        self.count = count

    def run(self) :
        # self.parent.pgbTask.setRange(0, 100)
        # for i in range(0, 101) :
        #     print(f'print thread > {i}')
        #     self.parent.pgbTask.setValue(i)
        #     self.parent.txbLog.append(f'print thread > {i}')
        while self.working :
            self.procChanged.emit(f'print thread > {self.count}') # 시그널을 내보냄
            self.count += 1 # 값 증가만 
            time.sleep(0.0001)


class qtApp(QMainWindow) :
    def __init__(self) :
        super().__init__()
        uic.loadUi('./studyThread/threadApp.ui',self)
        self.setWindowTitle('THREAD APP v0.4')
        self.pgbTask.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)
        # init thread
        self.worker = BackgroungWorker(parent=self)
        # backgroundworke에 있는 시그널 접근 함수
        self.worker.procChanged.connect(self.procUpdated)

        self.pgbTask.setRange(0, 1000000)

    @pyqtSlot(int)
    def procUpdated(self, count) :
        self.txbLog.append(f'print thread > {count}')
        self.pgbTask.setValue(count)
        print(f'print thread > {count}')

    @pyqtSlot()
    def btnStartClicked(self):
        self.worker.start()
        self.worker.working = True

    def btnStartClicked(self) :
        th = BackgroungWorker(self)
        th.start()


if __name__ == '__main__' :    
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())