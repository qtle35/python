from math import sqrt



def check(n):
    s=str(n)
    if len(s)<2: return False
    for i in range(1,len(s)):
        if s[i]!=s[len(s)-i-1]: return False
    return True

n, m = [int(x) for x in input().split()]
k = 0
a = []
ma = -1
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
    for i in range(m):
        if b[i]>ma and check(b[i]): ma=b[i]

for i in range(n):
    for j in range(m):
        if a[i][j] == ma:
            if k==0: print(ma)
            print("Vi tri [%d][%d]" % (i, j))
            k = 1
if k == 0:
    print('NOT FOUND')
