# DemoStr.py
#print(dir(str))

strA = "파이썬은 강력해"
strB = "python is very powerful"
print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.startswith("py"))
print(strB.endswith("ful"))
print(strB.endswith("ful", 7))
print(strB.count("p"))
print(strB.count("p", 7))

print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

u = "<<< spam and ham >>>"
#앞뒤에 있는 어떤 문자 
result = u.strip("<> ") 
print(u)
print(result)

result = result.replace("spam", "spam egg")
print(result)
lst = result.split()
print(lst)
print(":)".join(lst))


