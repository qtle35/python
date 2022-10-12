t= int(input())
def check(a,b):
    for i in range(0,len(a)):
        if a[i]>b[i]: return False
    return True
while t>0:
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    a.sort()
    b.sort()
    if check(a,b): print("YES")
    else: print("NO")
    t-=1