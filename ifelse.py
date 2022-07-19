# ifelse.py
# 다중라인으로 주석 처리: ctrl + / (cmd + /)
# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

#반복문
value = 5 
while value > 0:
    print(value)
    value -= 1 

print("---for in---")
lst = [1,2,3]
for item in lst:
    print(item)

lst = list(range(1,11))
print(lst)
for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))

print("---continue구문---")
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

print("---range함수---")
print(list(range(2000,2023)))
print("---리스트 내장(임베딩, 컴프리헨션)---")
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])
tp = ("apple","kiwi","banana")
print([len(i) for i in tp])

print("---필터링---")
lst = [10,25,30]
#다른 언어의 null(None)
iterL = filter(None, lst)
for item in iterL:
    print(item)

#조건이 되는 함수 정의
def getBiggerThan20(i):
    return i > 20 

print("---필터링 함수 사용---")
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("---람다 함수 사용---")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)
