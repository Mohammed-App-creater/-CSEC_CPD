
col = 0
moves = 0
for i in range(5):
    row = str(input())
    if row.find("1") != -1:
        row = row.split()
        moves =abs(2 - col) + abs(2 - int(row.index("1")))
    else:   
        col += 1
    
print(moves)


