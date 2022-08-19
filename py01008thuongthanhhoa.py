from curses.ascii import isupper


s=input()
hoa=0;thuong=0
for i in range(0,len(s),1):
    if s[i].isupper(): hoa+=1
    else: thuong+=1
if hoa>thuong: print(s.upper())
else: print(s.lower())