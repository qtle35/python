
from operator import attrgetter


class sv:
    def __init__(self,ten,dung,sub):
        self.ten = ten;
        self.dung   = dung;
        self.sub = sub;
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
    a = sorted(a, key= lambda sv: (-sv.dung, sv.sub, sv.ten))
print(*a,sep='\n')
