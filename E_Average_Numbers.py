num = int(input())
a = list(map(int, input().split()))
l = []
alsum = sum(a)
for i in range(num):
    if (alsum - a[i])/(num-1) == a[i] :
        l.append(str(i+1))
m = len(l)
if m == 0:
    print(0)
else:
    print(m)
    print(" ".join(l))