

n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(*sorted(list(set(a).intersection(set(b)))))
print(*sorted(list(set(a).difference(set(b)))))
print(*sorted(list(set(b).difference(set(a)))))
