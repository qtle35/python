from typing import Counter


s=input()
b=Counter()
while len(s)>1:
    n=int(s[0:2])
    s=s[2:]
    b[n]+=1
for i in b.keys():
    print("%d %d"%(i,b[i]))