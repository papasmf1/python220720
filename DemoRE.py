# DemoRE.py
import re 

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())

