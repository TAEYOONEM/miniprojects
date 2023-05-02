import cv2
import threading
import sys

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import uic

class qtApp(QMainWindow):
    def __init__(self) :
        super().__init__()
        uic.loadUi('/home/team5/camera/test1.ui',self)
        self.running = False
        self.start()

    def run(self):
        cap = cv2.VideoCapture(-1)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.label.resize(width, height)
        while self.running:
            ret, img = cap.read()
            if ret:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h,w,c = img.shape
                qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qImg)
                self.label.setPixmap(pixmap)
            else:
                print("cannot read frame.")
                break
        cap.release()
        print("Thread end.")

    def start(self) :
        self.running = True
        th = threading.Thread(target=self.run)
        th.start()
        print("started..")

if __name__ == '__main__' :    
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())
