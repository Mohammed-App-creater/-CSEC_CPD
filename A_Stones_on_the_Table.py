num = int(input())
st =input()
c=0
for i in range(num-1):
    if(st[i]==st[i+1]):
        c+=1
print(c)