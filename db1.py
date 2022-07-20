# db1.py 
import sqlite3

#연결객체 리턴(일단은 임시로 메모리에서 작업)
con = sqlite3.connect(":memory:")
#커서 객체(SQL구문을 실행하는 객체)
cur = con.cursor()
#테이블 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick','010-111');")
#외부에서 입력 파라메터로 처리 
name = "gildong"
phoneNumber = "010-222"
#입력 파라메터 처리
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
#다중의 데이터 입력(2차원 행렬)
datalist = (("tom","010-123"), ("dsp","010-456"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)



