from math import gcd


t=int(input())
while t>0:
    a=int(input())
    b=int(input())
    print(gcd(a,b))
    t-=1
