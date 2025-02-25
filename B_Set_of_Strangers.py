num = int(input())
for _ in range(num):
    r,c = map(int,input().split())
    l = []
    b = {}
    for i in range(r):
        row = input().split()
        l.extend(row)
    for n in l:
        if n in b:
            b[n] += 1
        else:
            b[n] = 1
    print((len(l)- (len(l) - max(b.values()))), max(b.values()), len(l))