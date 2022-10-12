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
    sum1=0
    sum2=0
    for i in range(len(n)-3,len(n)):
        sum1=sum1*10+int(n[i])
    for i in range(0,3):
        sum2=sum2*10+int(n[i])
    if(prime(sum1) and prime(sum2)): print("YES")
    else: print("NO")