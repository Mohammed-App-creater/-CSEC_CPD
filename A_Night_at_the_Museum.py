ma = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
m = input()
curr, total = 1, 0
forward, backward = 0, 0
for i in m:
    cc = 0
    n = ma.index(i) + 1
    if n > curr:
        cc = (n - curr)
    else:
        cc = (curr - n)
    total += min(cc, 26 - cc)
    curr = n
    
print(total)

