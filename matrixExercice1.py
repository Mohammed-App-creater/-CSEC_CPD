num = 5
for i in range(num+1):
    for j in range(1, i+1, 1):
        print(j, end=" ")
    print()
for i in range(num+1):
    s = "  "*i
    for j in range(i+1, num+1, 1):
        s += str(j )
        s += " " 
    print(s , end=" ")
    print()
    
