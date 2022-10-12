from typing import Counter


s=input()
m=int(input())
b=Counter()
se=set()
k=0
while len(s)>1:
    n=int(s[0:2])
    s=s[2:]
    b[n]+=1
    se.add(n)
se=sorted(se)
for i in se:
    if b[i]>=m: 
        k=1
        print(i,b[i])
if k==0: print('NOT FOUND')