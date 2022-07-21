# DemoButton.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#디자이너 없이 작업한 파일 
class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        btn1 = QPushButton("닫기", self)
        #좌측 상단(x축, y축)
        btn1.move(20, 20)
        #해당 위젯의 시그널에 슬롯 메서드를 연결
        btn1.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_() 