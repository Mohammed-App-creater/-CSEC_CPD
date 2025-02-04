wight = input().split()
a = int(wight[0])
b = int(wight[1])
years = 0

while a <= b:   
    a = a * 3
    b = b * 2
    years = years + 1
    
print(years)