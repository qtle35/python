from dataclasses import replace


s = input()
i = 0
while True:
    if '688' in s and s.find('688')==0:
        s = s.replace('688', '', 1)
    elif '68' in s and s.find('68')==0:
        s = s.replace('68', '', 1)
    elif '6' in s and s.find('6')==0:
        s = s.replace('6', '', 1)
    else:
        break
print('YES') if s == '' else print('NO')
