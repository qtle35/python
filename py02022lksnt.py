from math import sqrt



def nt(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1,1):
        if n%i==0: return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
b=[0]*1000005  
for i in range(0,n-1):
    dem=1
    if nt(a[i]) and b[a[i]]==0:
        for j in range(i+1,n):
            if a[i]==a[j]:
                b[a[j]]=1
                dem+=1
        print(a[i],dem)