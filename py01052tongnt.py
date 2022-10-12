
from math import sqrt


t= int(input())
def check(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1,1):
        if n%i==0: return False
    return True
while t>0:
    s=input()
    sum=0
    for i in range(0,len(s),1):
        sum+=int(s[i])
    if check(sum): print("YES")
    else: print("NO")
    t-=1