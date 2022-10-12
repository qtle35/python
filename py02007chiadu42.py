test=10
s= set()
while test>0:
    data=[int(x) for x in input().split()]
    for i in range(0,len(data)):
        s.add(data[i]%42)
    test-=len(data)
print(len(s))