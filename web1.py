# web1.py 
# 웹 크롤링을 위한 라이브러리
from bs4 import BeautifulSoup
#페이지 로딩(메서드 체인)
page = open("test01.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#find_all()메서드
#<p> 전체를 검색 
#print(soup.find_all("p"))
#<a>태그 
#print(soup.find_all("a"))
#find()는 한개를 검색 
#print(soup.find("p"))
#필터링: <p class='outer-text'>인 경우
#파이썬 키워드로 class와 충돌발생 
#print(soup.find_all("p", class_='outer-text'))
#태그의 내부 문자열을 리턴
for tag in soup.find_all("p"):
    title = tag.text.strip() 
    title = title.replace("\n", "")
    print(title)




