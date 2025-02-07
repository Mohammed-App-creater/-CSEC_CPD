num = int(input())
colors = []
count = 0
for i in range(num):
    colors.append(  [int(x) for x in input().split()])
for i in range(num):
    for j in range(i+1, num):
        if colors[i][0] == colors[j][1]:
            count += 1
        if colors[i][1] == colors[j][0]:
            count += 1
print(count)