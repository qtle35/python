from math import sqrt


t= int(input())
def nt(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1,1):
        if n%i==0: return False
    return True
while t>0:
    s=input()
    if nt(len(s)):
        dem=0
        for i in range(0,len(s),1):
            if nt(int(s[i])): dem+=1
        if dem>len(s)-dem: print("YES")
        else: print("NO")
    else: print("NO")
    t-=1