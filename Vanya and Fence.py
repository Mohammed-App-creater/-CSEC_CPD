dic = input().split()
n = int(dic[0])
h = int(dic[1])

a = input().split()
b = 0
for i in range(n):
    if int(a[i]) <= h:
        b = b + 1
    else:
        b = b + 2
print(b)