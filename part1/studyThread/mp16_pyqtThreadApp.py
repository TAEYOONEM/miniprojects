import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

MAX = 1000

class BackgroungWorker(QThread) : # PyQt5 스레드를 위한 클래스 존재
    procChanged = pyqtSignal(int) # 커스텀 시그널 (마우스 클릭같은 시그널을 따로 만드는 것)

    def __init__(self, count = 0 ,parent = None) -> None:
        super().__init__()
        self.main = parent
        self.working = False # 스레드 동작여부
        self.count = count

    def run(self) : # thread.start() --> run()
        # self.parent.pgbTask.setRange(0, 100)
        # for i in range(0, 101) :
        #     print(f'print thread > {i}')
        #     self.parent.pgbTask.setValue(i)
        #     self.parent.txbLog.append(f'print thread > {i}')
        while self.working :
            if self.count <= MAX :
                self.procChanged.emit(self.count) # 시그널을 내보냄
                self.count += 1 # 값 증가만 // 업무프로세스 동작하는 위치
                time.sleep(0.0001) # 세밀하게 주면 GUI처리를 제대로 못함
            else :
                self.working = False # 멈춤

class qtApp(QMainWindow) : 
    def __init__(self) :
        super().__init__()
        uic.loadUi('./studyThread/threadApp.ui',self)
        self.setWindowTitle('THREAD APP v0.4')
        self.pgbTask.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)
        # init thread
        self.worker = BackgroungWorker(parent=self, count= 0)
        # backgroundworke에 있는 시그널 접근 함수
        self.worker.procChanged.connect(self.procUpdated)
        self.pgbTask.setRange(0, MAX)

    # @pyqtSlot(int)
    def procUpdated(self, count) :
        self.txbLog.append(f'print thread > {count}')
        self.pgbTask.setValue(count)
        print(f'print thread > {count}')

    # @pyqtSlot()
    def btnStartClicked(self):
        self.worker.start() # 스레드 클래스 run() 실행
        self.worker.working = True
        self.worker.count = 0 # 

if __name__ == '__main__' :    
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())