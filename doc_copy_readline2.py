#정규표현식 패턴 
import re 

f=open('PV3.txt','rt')
g=open('PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일(1GB)이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''):
    if (re.search("error", line)):
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()








