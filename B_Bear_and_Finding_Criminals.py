cites, ints = map(int, input().split())

m = list(map(int, input().split()))


l,r = ints-2, ints
count =0
if m[ints-1] == 1:
    count += 1
for i in range(1,cites):
    if (l < 0 and r<cites ) and m[r] > 0:
        count += 1
    elif (r >= cites and l>=0) and m[l] > 0:
        count += 1
    elif (r < cites and l>=0) and m[l] > 0 and m[r] > 0:
        count += 2
    l -= 1
    r += 1
print(count)