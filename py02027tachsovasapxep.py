import re


t=int(input())
a=[]
while t>0:
    s=re.findall('[0-9]+',input())
    for i in range(0,len(s)):
        a.append(int(s[i]))
    t-=1
a.sort()
print(*a,sep='\n')