num  = int(input())
for _ in range(num):
    n,m,k = map(int, input().split())
    a = list( input())
    b = list( input())
    a.sort()
    b.sort()
    c = ""
    an, bn = 0, 0
    while len(a) > 0 and len(b) >0:
        if a[0] < b[0]:
            if an < k:
                c += str(a.pop(0))
                an += 1
                bn = 0
            else:
                c += str(b.pop(0))
                bn += 1
                an = 0
        else:
            if bn < k:
                c += str(b.pop(0))
                bn += 1
                an = 0
            else:
                c += str(a.pop(0))
                an += 1
                bn = 0
    print(c)