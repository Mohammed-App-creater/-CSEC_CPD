year = int(input())

while True:
    year += 1
    if len(set(str(year))) == 4:
        break
print(year)