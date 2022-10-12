from pickle import TRUE


t= int(input())
def check(s):
    id=0
    if len(s)<=2: return False
    for i in range(1,len(s),1):
        if(s[i]>s[i-1]): 
            id=i
            # print(i)
        elif s[i]==s[i-1]: return False
        else: break
    for i in range(id+1,len(s),1):
        if(s[i]<s[i-1]): 
            id=i
        elif s[i]==s[i-1]: return False
        else: break
    if(id!=len(s)-1): return False
    return True
while t>0:
    s=input()
    if check(s): print("YES")
    else: print("NO")
    t-=1