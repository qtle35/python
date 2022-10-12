from itertools import combinations, permutations

n,k=[int(x) for x in input().split()]
m=[int(x) for x in input().split()]
b=[0]*1005
a=[]
for i in range(0,n):
    if b[m[i]]!=1:
        b[m[i]]=1
        a.append(m[i])
a.sort()
s2=combinations(a,k)
for i in s2:
    print(*i,sep=' ')