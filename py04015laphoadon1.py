import math


class hoadon:
    def __init__(self, id, ten, cu, moi):
        self.id = id
        self.ten = ten
        self.cu = cu
        self.moi = moi
        self.dif = moi - cu

    def tinh(self):
        sum = 0
        if self.dif <= 50:
            self.tong = self.dif*100*1.02
        elif self.dif <= 100:
            self.tong = (50*100+(self.dif-50)*150)*1.03
        else:
            self.tong = (50*100+50*150+(self.dif-100)*200)*1.05

    def __str__(self):
        return f'{self.id} {self.ten} {math.ceil(self.tong)}'


l = []
for i in range(int(input())):
    a = hoadon('KH%02d' % (i+1),input(), int(input()), int(input()))
    a.tinh()
    l.append(a)
l = sorted(l, key=lambda x: x.tong, reverse=True)
print(*l, sep='\n')
