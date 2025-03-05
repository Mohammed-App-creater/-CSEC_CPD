num = int(input())
for _ in range(num):
    l=[]  
    n = int(input())
    for i in range(n):
        s = input()
        l.append(str(s.index('#')+1))
    l.reverse()
    print(" ".join(l))