# DemoFile.py
print("---정렬방식---")
for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---왼쪽정렬---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("---0으로채우기---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(3))



