import re


t= int(input())
for i in range(t):
    s = input()
    a = [int(x) for x in re.findall('[0-9]+',s)]
    print(min(a))