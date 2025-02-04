n = int(input());
win = input().split()

a = 0
for i in win:
    if (i == "A"):
        a+=1
    else:
        a-=1

if a > 0:
    print("Anton")
elif a < 0:
    print("Danik")
else:
    print("Friendship")