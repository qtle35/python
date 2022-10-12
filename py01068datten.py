from itertools import combinations


n,k=[int(x) for x in input().split()]
s=input().split()
b=set(s)
b=sorted(b)
res=combinations(b,k)
for i in list(res):
    print(*i)
