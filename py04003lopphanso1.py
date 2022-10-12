from math import gcd


class Phanso:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def rutgon(self):
        tu=self.x/gcd(self.x,self.y)
        mau=self.y/gcd(self.x,self.y)
        return str(int(tu)) + "/" +str(int(mau))

if __name__ == '__main__':
    x,y=[int(x) for x in input().split()]
    a=Phanso(x,y)
    print(a.rutgon())