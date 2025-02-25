num = int(input())
st = input()
s=""
if num%2 == 0:
    s = st[0]
    for i in range(1,num):
        if i %2 == 0:
            s = st[i] + s
            
        else:
            s = s + st[i]
else:
    for i in range(num):
        if i %2 != 0:
            s = st[i] + s
            
        else:
            s = s + st[i]
print(s)