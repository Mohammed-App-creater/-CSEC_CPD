n = int(input()) 
a = list(map(int, input().split()))
s = int(input())
for i in range(s):
    w, b = map(int, input().split())
    w,b = int(w),int(b)
    if w ==1:
            a[w] += a[w-1] - b
    elif w == n:
            a[w-2] += b - 1
    else:
            a[w-2] += b - 1
            a[w] += a[w-1] - b
    a[w-1] = 0
for i in a:
    print(i)
