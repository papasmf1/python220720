# DemoFile.py
print("---정렬방식---")
for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽정렬---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("---0으로채우기---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(3))


print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

url = "http://www.credu.com/?page=" + str(1) 
print(url)

#파일을 생성 
f = open("demo.txt", "wt")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일을 읽어서 처리
f = open("demo.txt", "rt")
result = f.read()
print(result)
f.close() 
