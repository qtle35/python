
from operator import attrgetter


class sv:
    def __init__(self,ten,dung,sub):
        self.ten = ten;
        self.dung   = dung;
        self.sub = sub;
    # def __repr__(self):
    #     return repr(self.ten,self.dung,self.sub)
    def __str__(self):
        return f'{self.ten} {self.dung} {self.sub}'


def multisort(xs, specs):
        for key, reverse in reversed(specs) :
            xs.sort(key=attrgetter(key), reverse=reverse)
        return xs

t = int(input())
a=[]
while t>0:
    t-=1
    s = input()
    x,y = [int(x) for  x in input().split()]
    a.append(sv(s,x,y))
multisort(a,(('dung',True),('sub',False),('ten',False)))
print(*a,sep='\n')
# for i in range(0,len(a)):
#     print(a[i].__str__())
