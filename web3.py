# web2.py 
#웹서버와 통신할 경우 
import urllib.request
#클로링
from bs4 import BeautifulSoup

#파일로 저장
f = open("webtoon.txt", "wt", encoding="utf-8")
#페이징 처리를 위해 range()함수 사용
#에러 처리 
try: 
    for i in range(1,11):
        url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
        print(url)
        data = urllib.request.urlopen(url) 
        soup = BeautifulSoup(data, "html.parser")
        #특정한 태그를 검색
        cartoons = soup.find_all("td", class_="title")
        for item in cartoons:
            item2 = item.find("a")
            title = item2.text.strip()
            print(title)
            f.write(title + "\n")
except:
    pass 

f.close()
print("웹 크롤링 종료")
