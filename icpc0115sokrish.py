
t= int(input())
def gt(n):
    giai_thua = 1
    if (n == 0 or n == 1):
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua
while t>0:
    s=input()
    sum=0
    for i in range(0,len(s),1):
        sum+=gt(int(s[i]))
    if str(sum)==s: print("Yes")
    else: print("No")
    t-=1