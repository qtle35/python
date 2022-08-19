t=int(input())
while t>0:
    n=int(input())
    print("1 ",end="")
    for i in range(2,n+1,1):
        dem=0
        if n%i==0:
            while n%i==0:
                dem+=1
                n/=i
            print(" * ",end="")
            print(i,end="")
            print("^",end="")
            print(dem,end=" ")
    print("")
    t-=1