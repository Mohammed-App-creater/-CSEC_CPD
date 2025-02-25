num = int(input())
for i in range(num):
    a,b,c = map(int,input().split())    
    if (a > b and a < c) or (a < b and a > c):
        print(a)
    elif (a > b and b > c) or (a < b and b < c):
        print(b)
    elif (a < c and c < b) or (a > c and c > b):
        print(c)