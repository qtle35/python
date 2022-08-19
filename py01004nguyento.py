from math import *


t=int(input())
def nt(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1,1):
        if n%i==0: return False
    return True
while t>0:
    n=int(input())
    dem=0
    for i in range(1,n,1):
        if gcd(i,n)==1: dem+=1
    if nt(dem): print("YES")
    else: print("NO")
    t-=1
    