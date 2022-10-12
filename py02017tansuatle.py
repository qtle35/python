from typing import Counter


t = int(input())

while t > 0:
    a = Counter()
    n = int(input())
    b = [int(x) for x in input().split()]
    for i in range(n):
        a[b[i]] += 1
    for i in range(n):
        if a[b[i]] % 2 != 0:
            print(b[i])
            break
    t -= 1
