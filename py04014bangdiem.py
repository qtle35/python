from statistics import mean


class Sv:

    

    def __init__(self, ma, ten, av):

        def xx(aver):
            if (aver >= 9):
                return 'XUATSAC'
            elif (aver >= 8):
                return 'GIOI'
            elif (aver >= 7):
                return 'KHA'
            elif (aver >= 5):
                return 'TB'
            else:
                return 'YEU'
        self.ten = ten
        self.av = av
        self.loai = xx(av)
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.gpa} {self.loai}'


t = int(input())
l = []
for i in range(1, t+1):
    s = input()
    a = [float(x) for x in input().split()]
    l.append(Sv('HS'+str(i),s, (mean(a)*100+1)/100))
l = sorted(l, key= lambda Sv: -Sv.av)
print(l)
