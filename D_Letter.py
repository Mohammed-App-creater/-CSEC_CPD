h,w = map(int,input().split())
arr =  [input().strip() for _ in range(h)]
top, bottom = h, 0
left, right = w, 0


for i in range(h):
    for j in range(w):
        if arr[i][j] == '*':
            top = min(top, i)
            bottom = max(bottom, i)
            left = min(left, j)
            right = max(right, j)

for i in range(top, bottom + 1):
    print(arr[i][left:right + 1])
