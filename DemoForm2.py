# DemoForm2.py 
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#폼디자인을 로딩(2번폼)
form_class = uic.loadUiType("DemoForm2.ui")[0]

#클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯 메서드
    def firstClick(self):
        self.label.setText("첫번째 클릭")
    #슬롯 메서드
    def secondClick(self):
        self.label.setText("두번째 클릭~~")
    #슬롯 메서드
    def thirdClick(self):
        self.label.setText("세번째 클릭을 했습니다.")

#진입점을 체크
#if __name__ == "__main__":
app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show() 
app.exec_() 