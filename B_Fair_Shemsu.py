#ICPC_A_Mohammed-Ismail
a,b = map(int,input().split())
l=[]
if a % b ==0:
    print((str(a//b)+" ")*b)
elif a % b != 0:
    x = a%b
    print((str(a//b)+" ")*(b-(a%b)) +(str(a//b+1)+" ")*(b-(b-(a%b))))