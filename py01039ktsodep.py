t= int(input())
def check(s):
    for i in range(2,len(s),2):
        if s[i]!=s[i-2]: return False
    for i in range(3,len(s),2):
        if s[i]!=s[i-2]: return False
    return True
while t>0:
    s=input()
    if check(s): print("YES")
    else: print("NO")
    t-=1