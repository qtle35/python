
from math import sqrt

t=int(input())
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
while t>0:
    s=input()
    k=1
    for i in range(0,len(s)):
        if prime(i):
            if prime(int(s[i]))==False:
                print("NO")
                k=0
                break
        else:
            if prime(int(s[i])):
                print("NO")
                k=0
                break
    if k==1: print("YES")
    t-=1