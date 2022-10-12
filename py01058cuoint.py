from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
t = int(input())
for i in range(t):
    n = input()
    sum=0
    for i in range(len(n)-4,len(n)):
        sum=sum*10+int(n[i])
    if(prime(sum)): print("YES")
    else: print("NO")