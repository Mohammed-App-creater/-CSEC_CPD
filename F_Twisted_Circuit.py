l = []
for i in range(4):
    l.append(int(input()))
d,c,b,a = 0,1,1,0
sol = ((a | b) & (c ^ d)) | ((b | c) ^ (a | d))
print(sol)