pric, r = map(int, input().split())
count, newpr = 1, pric
while count < 11:
    if newpr % 10 == 0 or newpr % 10 == r:
        print(count)
        break
    newpr += pric
    count += 1