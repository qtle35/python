t=int(input())
while t>0:
    s=input()
    k=1
    sum=0
    mul=1
    for i in range(0,len(s)):
        if i%2!=0: sum+=int(s[i])
        elif i%2==0 and s[i]!="0": mul*=int(s[i])
    print("%d %d"%(mul,sum))
    t-=1