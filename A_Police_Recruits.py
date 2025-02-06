num = int(input())
cf = input().split()
crim, count =  0, 0
for i in range(num):
    if crim < 0 and int(cf[i]) > 0:
        crim  = 0
    crim += int(cf[i])
    if crim < 0:
        count += 1
print(count)