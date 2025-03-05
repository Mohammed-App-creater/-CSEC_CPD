amount = int(input())
bills = [100, 20, 10, 5, 1]
count = 0
for bill in bills:
    count += amount // bill
    amount %= bill
print(count)