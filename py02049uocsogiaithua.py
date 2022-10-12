t=int(input())
while t>0:
    n,k=[int(x) for x in input().split()]
    dem=0
    for i in range(2,n+1):
        m=i
        while m%k==0:
            dem+=1
            m/=k
    print(dem)
    t-=1