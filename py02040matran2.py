
n=int(input())
a=[]
for i in range(0,n):
    b=[int(x) for x in input().split()]
    a.append(b)
k=int(input())
sum_up=0
sum_down=0
for i in range(0,n):
    for j in range(0,n-i):
        sum_up+=a[i][j]
for i in range(0,n):
    for j in range(n-i-1,n):
        sum_down+=a[i][j]
if abs(sum_up-sum_down)<=k: 
    print("YES")
    print(abs(sum_up-sum_down))
else:
    print("NO")
    print(abs(sum_up-sum_down))
