from datetime import datetime


class khach:

    def __init__(self, ma, ten, timeplay):
        self.ma = ma
        self.ten = ten
        self.timeplay = timeplay

    def __str__(self):
        return f'{self.ma} {self.ten} {int(self.timeplay/60)} gio {int(self.timeplay%60)} phut'


t = int(input())
a = []
while t > 0:
    t -= 1
    timeformat = '%H:%M'
    a.append(khach(input(),input(),  24*60 - (((datetime.strptime(input(), timeformat)) - datetime.strptime(input(), timeformat)).seconds)/60 ))


a = sorted(a, key=lambda khach: khach.timeplay, reverse=True)
print(*a, sep='\n')
