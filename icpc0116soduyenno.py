
from math import sqrt


t= int(input())
def check(n):
    if s[0]==s[len(s)-1]: return True
    return False
while t>0:
    s=input()
    if check(s): print("YES")
    else: print("NO")
    t-=1