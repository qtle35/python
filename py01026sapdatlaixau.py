from re import T


n=int(input())
for i in range(1,n+1):
    s1=input()
    s2=input()
    s1=sorted(s1)
    s2=sorted(s2)
    print("Test %d: "%i,end="")
    print('YES') if s1==s2 else print('NO')