


t=int(input())
while t>0:
    n=int(input())
    a=[int(x) for x in input().split()]
    b=set(a)
    if min(a)==max(a): print(0)
    else: print(max(a)-min(a)+1-len(b))
    t-=1
