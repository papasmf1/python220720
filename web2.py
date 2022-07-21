# web2.py 
#웹서버와 통신할 경우 
import urllib.request
#클로링
from bs4 import BeautifulSoup

#네이버에서 실행한 페이지결과를 문자열로 받기 
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체 
soup = BeautifulSoup(data, "html.parser")
#특정한 태그를 검색
cartoons = soup.find_all("td", class_="title")
# ctrl + / 
# <td class="title">
# 	<a href="/webtoon/detail">마음의 소리 50화 <격렬한 나의 하루> </a>
# </td>
print("갯수:{0}".format(len(cartoons)))
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)

for item in cartoons:
    item2 = item.find("a")
    title = item2.text.strip()
    print(title)
