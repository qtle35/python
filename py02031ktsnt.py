from math import sqrt



def nt(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1,1):
        if n%i==0: return False
    return True

n,m=[int(x) for x in input().split()]
a=[]
for i in range(0,n):
    b=[int(x) for x in input().split()]
    a.append(b)
for i in range(0,n):
    for j in range(0,m):
        if nt(a[i][j]): a[i][j]=1
        else: a[i][j]=0
        print(a[i][j],end=' ')
    print()
