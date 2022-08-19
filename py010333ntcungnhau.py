from math import gcd


l,r=[int(l) for l in input().split()]
for i in range(l,r+1,1):
    for j in range(i+1,r+1,1):
        for k in range(j+1,r+1,1):
            if gcd(i,j)==1 and gcd(j,k)==1  and gcd(i,k)==1: print("(%d, %d, %d)" % (i,j,k))