n = int(input())
wires = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1  
    
    left_birds = y - 1  
    right_birds = wires[x] - y  
    
    if x > 0:
        wires[x - 1] += left_birds  
    if x < n - 1:
        wires[x + 1] += right_birds  
    
    wires[x] = 0  
for i in wires:
        print(i)