def thay_doi_chu_so(a, p, q):
    for i in range(len(a)):
        if a[i] == p:
            a = a[:i] + q + a[i+1:]
    return int(a)

t = int(input())
for i in range(t):
    p, q = [p for p in input().split()]
    if p > q:
        p, q = q, p
        
    s = input().split()
    if len(s) == 1:
        a = s[0]
        b = input()
    else:
        a = s[0]
        b = s[1]
    # a = input()
    # b = input()
    print(thay_doi_chu_so(a, q, p)+thay_doi_chu_so(b, q, p), thay_doi_chu_so(a, p, q)+thay_doi_chu_so(b, p, q))