def check(n):
    for i in range(len(n)):
        if n[i]!='0' and n[i]!='1' and n[i]!='2': return False
    return True


t  = int(input())
for i in range(t):
    n = input()
    print('YES') if check(n) else print('NO')