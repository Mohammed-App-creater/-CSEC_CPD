clar = [int(x) for x in input().split()]
appr = input()
total = 0
for i in appr:
    total += clar[int(i)-1]
print(total)