num = int(input())
for _ in range(num):
    count = 0
    a, x, y = map(int, input().split()) 
    l = list(map(int, input().split())) 
    sm = sum(l)
    l.sort()
    for i in range(a):
        lr= l[::-1]
        n = l[0]
        h = sm - x - n
        lo = (sm - y - n)
        while h not in lr:
            h -= 1
        while l not in l:
            lo += 1
        lo = l.index(lo)
        h = lr.index(h)
        
        print((h-lo),lo,h,n)
        count += (h-lo)
        l.pop(0)        
    print(count)