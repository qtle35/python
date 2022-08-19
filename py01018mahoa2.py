p= "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    m=""
    x=[str(x) for x in input().split()]
    if x[0]=="0": break
    for i in range(0,len(x[1]),1):
         m+= p[(p.find(x[1][i])+int(x[0]))%28]
    print(m[::-1])