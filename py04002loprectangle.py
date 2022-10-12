class Rectangle:
    def __init__(self,dai,rong,mau):
        self.dai=dai
        self.rong=rong
        self.mau=mau.title()
    def perimeter(self):
        return (self.rong+self.dai)*2
    def area(self):
        return self.dai*self.rong
    def color(self):
        return self.mau


arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
if r.dai<=0 or r.rong<=0: print('INVALID')
else: print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))