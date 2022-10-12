t=int(input())
while t>0:
    n=int(input())
    b=[0]*1000005
    res=1000010
    mc=0
    a=[int(x) for x in input().split()]
    a.sort()
    for i in range(0,n):
        b[a[i]]+=1
        if b[a[i]]>mc :
            mc=b[a[i]]
            res=a[i]
    if mc>n/2: print(res)
    else: print("NO")
    t-=1