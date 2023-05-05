
def tich(n):
    tich = 1
    while n > 0:
        if int(n % 10) != 0:
            tich *= int(n % 10)
        n = int(n/10)
    return tich


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(0, n-2, 2):
        for j in range(i+2, n, 2):
            if tich(a[i]) > tich(a[j]):
                (a[i], a[j]) = (a[j], a[i])
            elif tich(a[i]) == tich(a[j]):
                if a[i] > a[j]:
                    (a[i], a[j]) = (a[j], a[i])
    for i in range(n):
        print(a[i], end=" ")
