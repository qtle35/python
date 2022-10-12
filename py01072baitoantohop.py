
n,k=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
a.sort
b=[]
for i in range(0,k+1):
    b.append(0)

def Try(i):
    for j in range(b[i-1]+1,n-k+i+1):
        b[i]=j
        if i==k:
            print(b)
            for l in range(1,k+1): print(a[b[i]-1],end=" ")
            print()
        else: Try(i+1)


Try(1)
