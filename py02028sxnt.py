from math import *


def nt(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1,1):
        if n%i==0: return False
    return True

n=int(input())
a=[int(x) for x in input().split()]
for i in range(0,len(a)-1):
    if nt(a[i]):
        for j in range(i+1,len(a)):
            if a[i]>a[j] and  nt(a[j]): a[i],a[j]=a[j],a[i]
print(*a)