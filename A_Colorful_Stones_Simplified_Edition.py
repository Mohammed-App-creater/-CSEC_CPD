pos = input()
ins = input()
p = 0
for i in range(len(ins)):
    if ins[i] == pos[p]:
        p += 1
print(p+1)