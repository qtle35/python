from typing import Counter


s=input()
b=Counter()
while len(s)>1:
    n=int(s[0:2])
    s=s[2:]
    b[n]+=1
a=[]
for i in b.keys():
    if b[i]!=0: a.append(i)
a.sort()
print(*a)