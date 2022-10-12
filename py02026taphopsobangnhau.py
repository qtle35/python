
def check(x,y):
    for i in range(0,len(x)):
        if x[i]!=y[i]: return False
    return True


n,m = [int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
x=set(a)
y=set(b)
x=sorted(x)
y=sorted(y)
if len(x)==len(y):
    if check(x,y): print('YES')
    else: print('NO')
else: print('NO')