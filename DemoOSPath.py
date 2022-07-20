# DemoOSPath.py
import random

print(random.random())
print(random.random())
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print("---샘플링---")
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))

#파일명을 다루는 경우
from os.path import * 
print(abspath("python.exe"))
print(basename("c:\\python39\\python.exe"))
print(getsize("c:\\python39\\python.exe"))

#운영체제 정보를 가져오는 경우
from os import * 
print("운영체제명:", name)
#system("notepad.exe")

#파일 리스트 
import glob 
result = glob.glob("c:\\work3\\*.py")
print(result)
