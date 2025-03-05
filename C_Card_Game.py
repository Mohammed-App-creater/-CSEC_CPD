num = int(input())
results = []

for _ in range(num):
    a, b, c, d = map(int, input().split())
    ply = [
        [(a, c), (b, d)],
        [(a, d), (b, c)],
        [(b, c), (a, d)],
        [(b, d), (a, c)],
    ]
    count = 0
    for game in ply:
        su = 0
        sl = 0
        for suc, slc in game:
            if suc > slc:
                su += 1
            elif slc > suc:
                sl += 1
        if su > sl:
            count += 1
    results.append(str(count))
print("\n".join(results))
    