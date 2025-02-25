num = int(input())
l = list(map(int, input().split()))
m = []
final = []
dr = {}

for i in range(num):
    if l[i] not in dr:
        dr[l[i]] = i
    else:
        m.append(dr[l[i]])
        dr[l[i]] = i
for i in range(num):
    if i not in m:
        final.append(str(l[i]))
print(len(final))
print(" ".join(final))