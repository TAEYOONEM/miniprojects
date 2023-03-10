# 주소록 GUI 프로그램 - MySQL 연동
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql

class qtApp(QMainWindow) :
    conn = None
    curIdx = 0 # 현재 데이터 PK
    
    def __init__(self) :
        super().__init__()
        uic.loadUi('./studyPyQt/addressBook.ui',self)
        self.setWindowIcon(QIcon('./studyPyQt/addressbook.png'))
        self.setWindowTitle('주소록 v0.5')
        self.initDB() # DB 초기화

        self.btnNew.clicked.connect(self.btnNewClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)
        self.tblAddress.doubleClicked.connect(self.tblAddressDoubleClicked)
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
                            db = 'miniproject', charset = 'utf8')
            query = 'DELETE FROM addressbook WHERE Idx = %s'
            cur = self.conn.cursor()
            cur.execute(query,(self.curIdx))

            self.conn.commit()
            self.conn.close()

            QMessageBox.about(self, '성공', '데이터를 삭제했습니다.')

            self.initDB()
            self.btnNewClicked()


    def btnNewClicked(self) :
        self.txtName.setText('')
        self.txtPhone.setText('')
        self.txtEmail.setText('')
        self.txtAddress.setText('')
        self.txtName.setFocus()
        self.curIdx = 0 # 0은 진짜 신규! 


    def tblAddressDoubleClicked(self) :
        rowIndex = self.tblAddress.currentRow()
        self.txtName.setText(self.tblAddress.item(rowIndex, 1).text())
        self.txtPhone.setText(self.tblAddress.item(rowIndex, 2).text())
        self.txtEmail.setText(self.tblAddress.item(rowIndex, 3).text())
        self.txtAddress.setText(self.tblAddress.item(rowIndex, 4).text())
        self.curIdx = int(self.tblAddress.item(rowIndex, 0).text())

    def btnSaveClicked(self) :
        fullName = self.txtName.text()
        phoneNum = self.txtPhone.text()
        email = self.txtEmail.text()
        address = self.txtAddress.text()

        if fullName == '' or phoneNum == '' :
            QMessageBox.warning(self, '주의', '이름과 핸드폰 번호를 입력하세요')
            return 
        else :
            # 4개 변수값 받아서 INSERT 쿼리문 만들기
            self.conn = pymysql.connect(host = 'localhost', user = 'root', password = '12345',
                            db = 'miniproject', charset = 'utf8')
            if self.curIdx == 0 :            
                query = '''INSERT INTO addressbook (fullName, PhoneNum, Email, Address)
                                VALUES (%s, %s, %s, %s)'''
            # UPDATE 쿼리문
            else :
                query = '''UPDATE addressbook
	                          SET FullName = %s
	                            , PhoneNum = %s
	                            , Email = %s
                                , Address = %s
                            WHERE Idx = %s'''

            cur = self.conn.cursor()
            if self.curIdx == 0 :
                cur.execute(query, (fullName, phoneNum, email, address))
            else :
                cur.execute(query, (fullName, phoneNum, email, address, self.curIdx))

            self.conn.commit()
            self.conn.close()

            # 저장성공 메시지
            if self.curIdx == 0 :
                QMessageBox.about(self, '성공', '저장성공')
            else :
                QMessageBox.about(self, '성공', '변경성공')

            self.initDB() # QTableWidget 새 데이터가 출력되도록
            self.btnNewClicked() # 입력창 내용 없어져

    def initDB(self) :
        self.conn = pymysql.connect(host = 'localhost', user = 'root', password = '12345',
                                    db = 'miniproject', charset = 'utf8')
        cur = self.conn.cursor()
        query = '''SELECT Idx
                        , FullName
	                    , PhoneNum
	                    , Email
	                    , Address
                     FROM addressbook'''

        cur.execute(query)
        rows = cur.fetchall()

        self.makeTable(rows)
        self.conn.close() # 프로그램 종료할 때

    def makeTable(self, rows) :
        self.tblAddress.setColumnCount(5)
        self.tblAddress.setRowCount(len(rows))
        
        self.tblAddress.setSelectionMode(QAbstractItemView.SingleSelection) # 단일선택
        self.tblAddress.setHorizontalHeaderLabels(['번호', '이름', '핸드폰', '이메일', '주소'])
        
        self.tblAddress.setColumnWidth(0, 0) # 1. 번호는 숨김
        self.tblAddress.setColumnWidth(1, 70) # 이름 열 70
        self.tblAddress.setColumnWidth(2, 105) # 핸드폰 열 105
        self.tblAddress.setColumnWidth(3, 175) # 이메일 열 175
        self.tblAddress.setColumnWidth(4, 200) # 주소 열 200
        
        self.tblAddress.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼 수정금지
        
        for i, row in enumerate(rows) :
            # row[0] ~ row[4]
            idx = row[0]
            fullName = row[1]
            phoneNum = row[2]
            email = row[3]
            addr = row[4]

            self.tblAddress.setItem(i, 0, QTableWidgetItem(str(idx)))
            self.tblAddress.setItem(i, 1, QTableWidgetItem(fullName))
            self.tblAddress.setItem(i, 2, QTableWidgetItem(phoneNum))
            self.tblAddress.setItem(i, 3, QTableWidgetItem(email))
            self.tblAddress.setItem(i, 4, QTableWidgetItem(addr))


if __name__ == '__main__' :    
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())