# function1.py
#함수 정의 
def times(a,b):
    return a+b, a*b 

#함수 호출
result = times(3,4)
print(result)

#함수 정의
def setValue(newValue):
    x = newValue
    print("함수 내부:", x)

#호출
result = setValue(5)
print(result)

#교집합을 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수로 리스트를 초기화 
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #어떤 글자가 postlist에 포함되어 있고 x가 result에 없으면 
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
print(intersect("HAM","SPAM"))