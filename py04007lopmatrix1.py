# import numpy as np
t = int(input())
# while t > 0:
#     t -= 1
#     n, m = [int(x) for x in input().split()]
#     a = []
#     for i in range(n):
#         a.append([int(x) for x in input().split()])
#     b = np.transpose(a)
#     res = np.dot(a, b)
#     for i in range(n):
#         print(*res[i])


while t > 0:
    t -= 1
    n, m = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    b = []
    for i in range(m):
        b.append([0]*n)
    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]
    res = [[sum(x * y for x, y in zip(a_row, b_col))
            for b_col in zip(*b)]
           for a_row in a]
    for i in res:
        print(*i)
