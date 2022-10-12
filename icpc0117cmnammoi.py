
t= int(input())
a=[]
dem=0
while t>0:
    s=input()
    if a.count(s)==0: dem+=1
    a.append(s)
    t-=1
print(dem)