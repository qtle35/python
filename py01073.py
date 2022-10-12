from itertools import permutations


s=input()
s2=permutations(s)
for i in s2:
    print(*i,sep='')