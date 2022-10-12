n, m = [int(x) for x in input().split()]
k = 0
a = []
mi = 1000000
ma = -1
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
    if max(b) > ma:
        ma = max(b)
    if min(b) < mi:
        mi = min(b)

for i in range(n):
    for j in range(m):
        if a[i][j] == ma-mi:
            if k==0: print(ma-mi)
            print("Vi tri [%d][%d]" % (i, j))
            k = 1
if k == 0:
    print('NOT FOUND')
