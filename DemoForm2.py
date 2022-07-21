# DemoForm2.py 
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹서버와 통신할 경우 
import urllib.request
#클로링
from bs4 import BeautifulSoup

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
        f = open("webtoon.txt", "wt", encoding="utf-8")
        try: 
            for i in range(1,11):
                url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" \
                    + str(i)
                print(url)
                data = urllib.request.urlopen(url) 
                soup = BeautifulSoup(data, "html.parser")
                cartoons = soup.find_all("td", class_="title")
                for item in cartoons:
                    item2 = item.find("a")
                    title = item2.text.strip()
                    print(title)
                    f.write(title + "\n")
        except:
            pass 
        f.close()
        self.label.setText("웹툰 크롤링 종료")
    #슬롯 메서드
    def secondClick(self):
        self.label.setText("두번째 클릭~~")
    #슬롯 메서드
    def thirdClick(self):
        self.label.setText("세번째 클릭을 했습니다.")


app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show() 
app.exec_() 