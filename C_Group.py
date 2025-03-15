num = int(input())
count = 0
for _ in range(num):
   l = list(map(int, input().split()))
   if sum(l) >= 2:
       count += 1
print(count)