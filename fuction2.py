# fuction2.py 
#불변형식 
a = 1.2 
print(id(a))
a = 2.3 
print(id(a))


print("---가변형식---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))