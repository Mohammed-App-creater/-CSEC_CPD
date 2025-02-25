num = int(input())
for i in range(num):
    l = list(map(int, input().split()))
    a = l[0]
    l.sort()
    print(4 -( l.index(a)+1))
