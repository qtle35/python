n = int(input())
a = [float(x) for x in input().split()]
mi = min(a)
ma = max(a)
sum = 0
dem = 0
for i in range(0, n):
    if a[i] != mi and a[i] != ma:
        sum += a[i]
        dem += 1
print("%.2f" % (sum/dem))
