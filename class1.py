# class1.py
#1)클래스 정의
class Person:
    #초기화 메서드(생성자)
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 
p1 = Person()
#3)인스턴스 메서드 호출
p1.print() 


