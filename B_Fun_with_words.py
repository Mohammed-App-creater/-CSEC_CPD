num = int(input())
n = []
l = []
for _ in range(num):
    n.append(int(input()))
    m = []
    for _ in range(num):
        m.append(input())
    l.append(m)

for i in range(num):
    a,b,c = 0,0,0
    for j in range(n[i]):
        ab = set(l[i][j]+l[i][j])

print(l, n)