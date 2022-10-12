from math import sqrt


t=int(input())
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def check(n):
    sum=0
    for i in range(0,len(n)):
        sum+=int(n[i])
        if i%2==0 : 
            if int(n[i])%2!=0: return False
            
        else:
            if int(n[i])%2==0: return False
    if(prime(sum)==False): return False
    return True
while t>0:
    n=input()
    if check(n): print("YES")
    else: print("NO")
    t-=1