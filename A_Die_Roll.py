a ,b = input().split()
c = 6 - max(int(a),int(b)) +1
dno = 6
if c % 2 == 0:
     c //= 2
     dno //= 2
if c % 3 == 0:
    c //= 3
    dno //= 3
print( str(c) + "/" + str(dno))