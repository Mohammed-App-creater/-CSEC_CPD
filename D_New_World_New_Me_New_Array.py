num = int(input())
for _ in range(num):
    count=0
    n,k,p = map(int, input().split())
    k = abs(k)
    if k == 0:
        print(0)
    elif k/p > n:
        print(-1)
    else:
        while k != 0 and p != 0:
            count += k//p
            k = k%p
            p -=1
        print(count if count != 0 else -1,)