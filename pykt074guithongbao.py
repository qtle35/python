t = int(input())
for c in range(t):
    s = input()
    if len(s) <= 100:
        print(s)
    else:
        if s[100] == " ":
            print(s[:100])
        else:
            s = s[:100].split()
            print(" ".join(s[:-1]))
