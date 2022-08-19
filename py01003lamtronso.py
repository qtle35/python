t=int(input())
while t>0:
    m=input()
    n=list(m)
    for i in range(len(n)-1,0,-1):
        a=int(n[i])
        if a>=5:
            n[i]=0
            n[i-1]=int(n[i-1])+1
        else:
            n[i]=0
    for i in n:
        print(i,end = "")
    print()
    t-=1
    