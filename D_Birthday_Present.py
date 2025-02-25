#ICPC_A_Mohammed-Ismail
num = int(input())

x = num*2+1
l = 1
mm =[]
w= 0

for i in range(x//2 +1):
    row = ["0"]
    rv =["0"]
    for n in range(1,l):
            row.append(str(n))
            rv = [str(n)] + rv
    l +=1
    w = len((row+rv[1:]))
    mm.append((row+rv[1:]))

w = w//2
for n,i in enumerate(mm):
    i = [" "]*(w-n) + i
    print(" ".join(i))
for i in range(len(mm)-2,-1,-1):
    mm[i] = [" "]*(w-i) + mm[i]
    print(" ".join(mm[i]))
    