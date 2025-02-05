num = int(input())
group =1
lis = []
for i in range(num):
  lis.append(input())
for i in range(num-1):
  if lis[i] != lis[i+1]:
    group += 1
print(group)