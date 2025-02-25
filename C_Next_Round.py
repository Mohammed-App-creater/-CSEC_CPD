num, v = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(num):
    if arr[i] >= arr[v-1] and arr[i] > 0:
        count += 1
    
print(count)