from typing import Counter


s=input()
c=Counter()
while len(s)>1:
    n=int(s[0:2])
    if c[n]==0:
        c[n]=1
        print(n,end=' ')
    s=s[2:]
    