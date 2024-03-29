# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Source\miniprojects\part1\studyPyQt\addressBook.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 24, 60, 12))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.txtName = QtWidgets.QLineEdit(self.groupBox)
        self.txtName.setGeometry(QtCore.QRect(90, 20, 191, 20))
        self.txtName.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhLatinOnly)
        self.txtName.setInputMask("")
        self.txtName.setPlaceholderText("")
        self.txtName.setObjectName("txtName")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 54, 60, 12))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.txtPhone = QtWidgets.QLineEdit(self.groupBox)
        self.txtPhone.setGeometry(QtCore.QRect(90, 50, 191, 20))
        self.txtPhone.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.txtPhone.setObjectName("txtPhone")
        self.txtEmail = QtWidgets.QLineEdit(self.groupBox)
        self.txtEmail.setGeometry(QtCore.QRect(90, 80, 191, 20))
        self.txtEmail.setObjectName("txtEmail")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 84, 60, 12))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.txtAddress = QtWidgets.QLineEdit(self.groupBox)
        self.txtAddress.setGeometry(QtCore.QRect(90, 110, 191, 20))
        self.txtAddress.setObjectName("txtAddress")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 114, 60, 12))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.btnNew = QtWidgets.QPushButton(self.groupBox)
        self.btnNew.setGeometry(QtCore.QRect(450, 100, 80, 30))
        self.btnNew.setObjectName("btnNew")
        self.btnSave = QtWidgets.QPushButton(self.groupBox)
        self.btnSave.setGeometry(QtCore.QRect(530, 100, 80, 30))
        self.btnSave.setObjectName("btnSave")
        self.btnDel = QtWidgets.QPushButton(self.groupBox)
        self.btnDel.setGeometry(QtCore.QRect(529, 68, 80, 30))
        self.btnDel.setAccessibleDescription("")
        self.btnDel.setStyleSheet("background-color:rgb(255,50,50);\n"
"color:rgb(255,255,255)")
        self.btnDel.setObjectName("btnDel")
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 169, 621, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tblAddress = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tblAddress.setObjectName("tblAddress")
        self.tblAddress.setColumnCount(0)
        self.tblAddress.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tblAddress)
        MainWindow.setCentralWidget(self.centralwidget)
        self.stbCurrent = QtWidgets.QStatusBar(MainWindow)
        self.stbCurrent.setObjectName("stbCurrent")
        MainWindow.setStatusBar(self.stbCurrent)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "정보입력"))
        self.label.setText(_translate("MainWindow", "이       름 : "))
        self.label_3.setText(_translate("MainWindow", "전화번호 : "))
        self.label_4.setText(_translate("MainWindow", "이  메 일 : "))
        self.label_5.setText(_translate("MainWindow", "주       소 : "))
        self.btnNew.setText(_translate("MainWindow", "신규"))
        self.btnSave.setText(_translate("MainWindow", "저장"))
        self.btnDel.setText(_translate("MainWindow", "삭제"))
