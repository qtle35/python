from math import sqrt



def nt(n):
    if n<2: return False
    for i in range(2,int(sqrt(n))+1,1):
        if n%i==0: return False
    return True

n, m = [int(x) for x in input().split()]
k = 0
a = []
ma = -1
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
    for i in range(m):
        if b[i]>ma and nt(b[i]): ma=b[i]

for i in range(n):
    for j in range(m):
        if a[i][j] == ma:
            if k==0: print(ma)
            print("Vi tri [%d][%d]" % (i, j))
            k = 1
if k == 0:
    print('NOT FOUND')
