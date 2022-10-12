import re


t=int(input())
while t>0:
    s=input()
    a=re.findall("[0-9]+",s)
    A=[int(x) for x in a]
    print(max(A))
    t-=1