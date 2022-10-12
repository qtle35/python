t=int(input())
while t>0:
    s1=input()
    so=0
    chuoi=""
    for i in range(0,len(s1)):
        if s1[i].isnumeric(): so+=int(s1[i])
        else: chuoi+=s1[i]
    print(*sorted(chuoi),so,sep='')
    t-=1
