t= int(input())
def check(s):
    sum=0
    sum+=int(s[0])
    for i in range(1,len(s),1):
        sum+=int(s[i])
        if abs(int(s[i])-int(s[i-1]))!=2: return False
    if sum%10!=0: return False
    return True
while t>0:
    s=input()
    if check(s): print("YES")
    else: print("NO")
    t-=1