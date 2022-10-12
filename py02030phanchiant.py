from math import *


def nt(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1,1):
        if n%i==0: return False
    return True

n=int(input())
a=[int(x) for x in input().split()]
c=[0]*1005
b=[]
for i in range(0,len(a)):
    if c[a[i]]==0:
        c[a[i]]=1
        b.append(a[i])
s=sum(b)
lsum=0
index=-1
for i in range(0,len(b)):
    lsum+=b[i]
    if nt(lsum) and nt(s-lsum):
        index=i
        break
if index==-1: print('NOT FOUND')
else: print(i)
