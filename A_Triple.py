num = int(input())

for _ in range(num):
    n =int(input())
    l = list(map( int, input().split()))
    if n < 3:
        print(-1)
        continue
    else:
        l.sort()
        i = 0
        value = -1
        while i < (len(l)-2):
            if l[i] == l[i+1] and l[i] == l[i+2]:
                value = l[i]
                break
            i += 1
        print(value)    
            