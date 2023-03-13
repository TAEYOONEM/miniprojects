# QR코드 생성앱
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qrcode

# QRCode 커스터마이징(이미지용 팩토리클래스) 클래스
# class Image(qrcode.image.base.BaseImage) :
#     def __init__(self, border, width, box_size) -> None:
#         self.border = border
#         self.width = width
#         self.box_size = box_size

#         size = (width + border * 2) * box_size

#         self._image = QImage(size, size, QImage.Format_RGB8)
#         self._image.fill(Qt.white) # 흰색
    
#     def pixmap(self) :
#         return QPixmap.fromImage(self._image)



class qtApp(QMainWindow) :
    def __init__(self) :
        super().__init__()
        uic.loadUi('./studyPython/qrcodeApp.ui',self)
        self.setWindowTitle('Qrcode 생성앱 v0.1')
        self.setWindowIcon(QIcon('./studyPython/qr-code.png'))

        self.btnQrGen.clicked.connect(self.btnQrgenClicked)
        self.txtQrData.returnPressed.connect(self.btnQrgenClicked)

    def btnQrgenClicked(self) :
        data = self.txtQrData.text()

        if data == '' :
            QMessageBox.warning(self,'경고','데이터를 입력하세요.')
            return
        else :
            qr_img = qrcode.make(data)
            qr_img.save('./studyPython/site.png')

            img = QPixmap('./studyPython/site.png')
            self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(300))

if __name__ == '__main__' :    
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())