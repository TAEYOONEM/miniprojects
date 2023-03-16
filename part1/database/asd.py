import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql


class qtApp(QMainWindow) :
    conn = None
    curIdx = 0 
    
    def __init__(self) :
        super().__init__()
        uic.loadUi('./database/carbook.ui',self)
        # self.setWindowIcon(QIcon('./studyPyQt/addressbook.png'))
        # self.setWindowTitle('주소록 v0.5')
        self.initDB()

        self.btnNew.clicked.connect(self.btnNewClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)
        self.tblcarinfo.doubleClicked.connect(self.tblcarinfoDoubleClicked) 
        self.btnDel.clicked.connect(self.btnDelClicked)

    def btnDelClicked(self) :
        if self.curIdx == 0:
            QMessageBox.warning(self,'경고','삭제할 테이터를 선택하세요')
            return 
        else :
            reply = QMessageBox.question(self, '확인', '삭제하시겠습니까?',QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes )
            if reply == QMessageBox.No :
                return
            self.conn = pymysql.connect(host = 'localhost', user = 'root', password = '12345',
                            db = 'carinfo', charset = 'utf8')
            query = 'DELETE FROM car WHERE carNum = %s'
            cur = self.conn.cursor()
            cur.execute(query,(self.curIdx))

            self.conn.commit()
            self.conn.close()

            QMessageBox.about(self, '성공', '데이터를 삭제했습니다.')

            self.initDB()
            self.btnNewClicked()

    def btnNewClicked(self) :
        self.txtCarNum.setText('')
        self.txtCarName.setText('')
        self.txtName.setText('')
        self.txtPhone.setText('')
        self.txtSubPhone.setText('')
        
        self.txtName.setFocus()
        self.curIdx = 0 


    def tblcarinfoDoubleClicked(self) :
        rowIndex = self.tblcarinfo.currentRow()
        
        self.txtCarNum.setText(self.tblcarinfo.item(rowIndex,0).text())
        self.txtCarName.setText(self.tblcarinfo.item(rowIndex, 1).text())
        self.txtName.setText(self.tblcarinfo.item(rowIndex, 2).text())
        self.txtPhone.setText(self.tblcarinfo.item(rowIndex, 3).text())
        self.txtSubPhone.setText(self.tblcarinfo.item(rowIndex, 4).text())
        
        self.curIdx = self.tblcarinfo.item(rowIndex, 0).text()

    def btnSaveClicked(self) :
        carNum = self.txtCarNum.text()
        carName = self.txtCarName.text()
        name = self.txtName.text()
        phone = self.txtPhone.text()
        subPhone = self.txtSubPhone.text()

        if carName == '' or carNum == '' or name == '' or  phone == '' :
            QMessageBox.warning(self, '주의', '차명, 차번, 성명, 휴대번호를 입력하시오.')
            return 
        else :
            self.conn = pymysql.connect(host = 'localhost', user = 'root', password = '12345',
                            db = 'carinfo', charset = 'utf8')
            if self.curIdx == 0 :            
                query = '''INSERT INTO car (carNum, carName, name, phone, subPhone)
                                VALUES (%s, %s, %s, %s, %s)'''

            else :
                query = '''UPDATE car
                              SET carNum = %s
	                            , carName = %s
	                            , name = %s
	                            , phone = %s
                                , subPhone = %s
                            WHERE carNum = %s'''

            cur = self.conn.cursor()
            if self.curIdx == 0 :
                cur.execute(query, (carNum, carName, name, phone, subPhone ))
            else :
                cur.execute(query, (carNum, carName, name, phone, subPhone, self.curIdx))

            self.conn.commit()
            self.conn.close()

            if self.curIdx == 0 :
                QMessageBox.about(self, '성공', '저장성공')
            else :
                QMessageBox.about(self, '성공', '변경성공')

            self.initDB() 
            self.btnNewClicked()

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

    def makeTable(self, rows) :
        self.tblcarinfo.setColumnCount(5)
        self.tblcarinfo.setRowCount(len(rows))
        
        self.tblcarinfo.setSelectionMode(QAbstractItemView.SingleSelection) 
        self.tblcarinfo.setHorizontalHeaderLabels(['차번', '차종', '이름', '휴대번호', '비상연락망'])
        
        self.tblcarinfo.setColumnWidth(0, 0) 
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
    


if __name__ == '__main__' :    
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())