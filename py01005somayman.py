t=int(input())
while t>0:
    n=input()
    kt=0
    for i in range(0,len(n),1):
        if n[i]!="4" and n[i]!="7":
            kt=1
            break
    if(kt==0): print("YES")
    else: print("NO")
    t-=1

