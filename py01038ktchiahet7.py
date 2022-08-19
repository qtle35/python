t=int(input())
while t>0:
    n=int(input())
    check=0
    for i in range(0,1000,1):
        if n%7==0:
            check=1
            print(n)
            break
        n=n+int(str(n)[::-1])
        
    if check==0: print('-1')
    t-=1