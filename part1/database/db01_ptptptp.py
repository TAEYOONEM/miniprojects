import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import pymysql

import pytesseract as tess
from PIL import Image

form_class = uic.loadUiType("C:/Source/miniprojects/part1/database/test.ui")[0]
tess.pytesseract.tesseract_cmd = r'C:/Dev/Tools/Tesseract-OCR/tesseract.exe'

class WindowClass(QMainWindow, form_class) :
    conn = None
    curIdx = 0 
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.initDB()
        self.btn_loadFromFile.clicked.connect(self.loadImageFromFile)

    def makeTable(self, rows) :
        self.tblcarinfo.setColumnCount(5)
        self.tblcarinfo.setRowCount(len(rows))
        
        self.tblcarinfo.setSelectionMode(QAbstractItemView.SingleSelection) 
        self.tblcarinfo.setHorizontalHeaderLabels(['차번', '차종', '이름', '휴대번호', '비상연락망'])
        
        self.tblcarinfo.setColumnWidth(0, 70) 
        self.tblcarinfo.setColumnWidth(1, 70) 
        self.tblcarinfo.setColumnWidth(2, 105)
        self.tblcarinfo.setColumnWidth(3, 175) 
        self.tblcarinfo.setColumnWidth(4, 200)  
        
        self.tblcarinfo.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        
        for i, row in enumerate(rows) :
            carNum = row[0]
            carName = row[1]
            name = row[2]
            phone = row[3]
            subPhone = row[4]

            self.tblcarinfo.setItem(i, 0, QTableWidgetItem(str(carNum)))
            self.tblcarinfo.setItem(i, 1, QTableWidgetItem(carName))
            self.tblcarinfo.setItem(i, 2, QTableWidgetItem(name))
            self.tblcarinfo.setItem(i, 3, QTableWidgetItem(phone))
            self.tblcarinfo.setItem(i, 4, QTableWidgetItem(subPhone))


    def initDB(self) :
        self.conn = pymysql.connect(host = 'localhost', user = 'root', password = '12345',
                                    db = 'carinfo', charset = 'utf8')
        cur = self.conn.cursor()
        query = '''SELECT
                          carNum
	                    , carName
	                    , name
	                    , phone
                        , subPhone
                     FROM car'''

        cur.execute(query)
        rows = cur.fetchall()

        self.makeTable(rows)
        self.conn.close() 

    def loadImageFromFile(self) :
        self.img = "C:/Source/miniprojects/part1/database/num2.png"
        
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(self.img)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(200)
        self.lblNum.setPixmap(self.qPixmapFileVar)

        result = tess.image_to_string(Image.open(self.img))

        self.conn = pymysql.connect(host = 'localhost', user = 'root', password = '12345',
                                db = 'carinfo', charset = 'utf8')
        
        cur = self.conn.cursor()
        query = f''' SELECT *
                      FROM car
                     WHERE carNum = {result}'''
        
        cur.execute(query)
        rows = cur.fetchall()

        self.makeTable(rows)
        self.conn.close() 

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 