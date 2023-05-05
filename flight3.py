import json
f = open('flights.json')
b = json.load(f)

t = int(input())
for test in range(t):
    a = input().split()
    sum = 0
    for i in b['flights']:
        if int(i['year']) >= int(a[0]) and int(i['year']) < int(a[1]):
            sum += int(i['passengers'])
    print('Invalid' if sum == 0 else sum)
