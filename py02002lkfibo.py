from math import gcd

f=[0,1]
def fibo():
    for i in range(2,94): f.append(f[i-1]+f[i-2])

t=int(input())
fibo()
while t>0:
    x,y=[int(x) for x in input().split()]
    for i in range(x,y+1):
        print(f[i],end=" ")
    print()
    t-=1
