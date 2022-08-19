from tokenize import Double


t=int(input())
while t>0:
    x, y, z = [float(x) for x in input().split()]
    for i in range(1,100,1):
        x+=x*y/100
        if x>=z:
            print(i)
            break
    t-=1