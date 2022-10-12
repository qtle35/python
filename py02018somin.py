n=int(input())
a=[int(x) for x in input().split()]
b=[0]*30005
for i in range(0,n):
    b[a[i]]=1

for i in range(1,30005):
    if b[i]!=1: 
        print(i)
        break
