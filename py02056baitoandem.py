

t=int(input())
b=[0]*2000
ma=0
k=0
while t>0:
    a=[int(x) for x in input().split()]
    if max(a)>ma: ma=max(a)
    for i in range(0,len(a)):
        b[a[i]]=1
    t-=len(a)

for i in range(1,ma+1):
    if b[i]==0: 
        print(i)
        k=1
if k==0: print('Excellent!')