t = int(input())
while t>0:
    t-=1;
    a,b,c,d = [int(x) for x in input().split()]
    x = complex(a,b)
    y = complex(c,d)
    re1 = (x+y)*x
    re2 = (x+y)**2
    print('{:.0f} {} {:.0f}i, {:.0f} {} {:.0f}i'.format(re1.real, '+-'[re1.imag<0], abs(re1.imag), re2.real, '+-'[re2.imag<0], abs(re2.imag)))