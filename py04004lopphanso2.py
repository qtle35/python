from math import gcd


class Phanso:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rutgon(self):
        mau = int(self.x/gcd(self.x, self.y))
        self.y = int(self.y/gcd(self.x, self.y))
        self.x=mau

    def cong(self, p):
        tu = self.x*p.y+p.x*self.y
        mau = self.y*p.y
        p2 = Phanso(tu, mau)
        p2.rutgon()
        return str(p2.x)+'/'+str(p2.y)

    def tu(self):
        return self.x

    def mau(self):
        return self.y


x, y, z, t = [int(x) for x in input().split()]
a = Phanso(x, y)
b = Phanso(z, t)
print(a.cong(b))
