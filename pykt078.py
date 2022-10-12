t = int(input())
while t > 0:
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    max_idex = a.index(max(a))
    a.insert(max_idex, m)
    for i in range(0, n+1):
        if a[i] < 0:
            print(a[i], end=' ')
    for i in range(0, n+1):
        if a[i] >= 0:
            print(a[i], end=' ')
    print()
    t -= 1
