def check(s):
    n=len(s)-1
    if s[n-2]=="." and s[n-1]=="p" and s[n]=="y": return True
    return False

s=input()
s=s.lower()
if check(s): print("yes")
else: print("no")
