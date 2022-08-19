t=int(input())
while t>0:
    s=input()
    for i in range(1,len(s),2):
        for j in range(0,int(s[i]),1):
            print(s[i-1],end="")
    print("")
    t-=1