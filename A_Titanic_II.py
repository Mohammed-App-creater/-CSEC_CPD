#ICPC_A_Mohammed-Ismail
mont = input()
num = int(input())
moths = [ "January", "February", "March", "April", "May", "June", 'July', "August", "September", 'October', 'November', "December"]

x = moths.index(mont)+1
ms = num +x
while ms > 12:
    ms-=12
print(moths[ms-1])
