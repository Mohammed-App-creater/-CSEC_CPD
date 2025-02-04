col = int(input());
numincols = [int(x) for x in input().split()];
numincols.sort()
ans = " ".join(str(x) for x in numincols)
print(ans)