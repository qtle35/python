s = input()
while len(s) != 1:
    n = int(s[0:int(len(s)/2)])+int(s[int(len(s)/2):])
    print(n)
    s = str(n)
