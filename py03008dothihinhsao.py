from collections import Counter


t=int(input())
c=Counter()
k=1
for test in range(t-1):
    x,y=[int(x) for x in input().split()]
    c[x]+=1
    c[y]+=1
    if c[x]==t-1 or c[y]==t-1: 
        k=0
        print("Yes")
if k==1: print("No")