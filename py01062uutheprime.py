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
    if(prime(len(n))):
        dem=0
        for i in range(0,len(n)):
            if prime(int(n[i])): dem+=1
        if dem>len(n)-dem: print("YES")
        else: print("NO")
    else: print("NO")