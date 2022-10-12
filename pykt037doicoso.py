t=int(input())
m='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while t>0:
    k,b=[int(x) for x in input().split()]
    s=''
    while k!=0:
        temp=int(k%b)
        k=int(k/b)
        s+=m[temp]
    print(s[::-1])
    t-=1