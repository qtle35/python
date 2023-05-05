from datetime import datetime


class hoadon:
    def __init__(self, id, ten, phong, nhan, tra, dichvu):
        self.id = id
        self.ten = ten
        self.phong = phong
        self.nhan = nhan
        self.tra = tra
        self.dichvu = dichvu

    def tinh(self):
        dfm = '%d/%m/%Y'
        ngaynhan = datetime.strptime(self.nhan, dfm)
        ngaytra = datetime.strptime(self.tra, dfm)
        self.dif = (ngaytra - ngaynhan).days + 1
        ma = self.phong[:1]
        if ma == '1':
            self.tien = self.dif*25+self.dichvu
        elif ma == '2':
            self.tien = self.dif*34+self.dichvu
        elif ma == '3':
            self.tien = self.dif*50+self.dichvu
        else:
            self.tien = self.dif*80+self.dichvu

    def __str__(self) -> str:
        return f'{self.id} {self.ten} {self.phong} {self.dif} {self.tien}'


l = []
for i in range(int(input())):
    a = hoadon('KH%02d' % (i+1), input().strip(), input().strip(),
               input().strip(), input().strip(), int(input().strip()))
    a.tinh()
    l.append(a)
l = sorted(l, key=lambda x: x.tien, reverse=True)
print(*l, sep='\n')
