
t= int(input())
def check(s):
    if len(s)<=1: return False
    for i in range(0,int(len(s)/2),1):
        if s[i]!=s[len(s)-i-1]: return False
    return True
while t>0:
    s=input()
    sum=0
    for i in range(0,len(s),1):
        sum+=int(s[i])
    if check(str(sum)): print("YES")
    else: print("NO")
    t-=1