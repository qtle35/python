t=int(input())
while t>0:
    n,d=[int(n) for n in input().split()]
    a=[int(x) for x in input().split()]
    a[:]=a[d:n]+a[0:d]
    for x in a:
        print(x,end=" ")
    print()
    t-=1