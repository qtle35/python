from math import *

def snt(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1,1):
        if n%i==0: return False
    return True
t=int(input())
while t>0:
    sum=0
    a,b = [int(a) for a in input().split()]
    m=str(gcd(a,b))
    for i in range(0,len(m),1):
        sum+=int(m[i])
    if snt(sum): print("YES")
    else: print("NO")
    t-=1
    
