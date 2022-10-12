t=int(input())
def check(a):
    for i in a:
        
        if not(i.isdigit()) or int(i)>=256: return False
    return True
while t>0:
    a=input().split('.')
    if len(a)==4:
        print('YES') if check(a) else print('NO')
    else:
        print('NO')
       
    t-=1