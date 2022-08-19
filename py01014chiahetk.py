a,k,n = [int(a) for a in input().split()]
dem=0
b=int(a/k)+1
for i in range(b,10000000,1):
    if i*k>n: break
    print(i*k-a, end=" ")
    dem=1
if dem==0: print('-1')