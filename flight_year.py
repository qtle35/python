import json

f = open('flight.json')
js = json.load(f)

for test in range(int(input())):
    nam, cs = input().split()
    l = []
    for i in js['flights']:
        if i['year'] == nam:
            l.append(int(i['passengers']))
    if cs == 'min':
        print(min(l))
    elif cs == 'max':
        print(max(l))
    elif cs == 'avg':
        print('%.5f' % (sum(l)/len(l)))
    else:
        print(sum(l))
