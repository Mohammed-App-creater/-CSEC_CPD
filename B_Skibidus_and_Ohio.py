num = int(input())
for _ in range(num):
    s = input()
    l = len(s)
    t = True
    for k in range(l-1):
        if s[k] == s[k+1]:
            s = s[:k] + s[k+1:]
            t = False
            
            break
    print(l) if t else print(1)
    
    