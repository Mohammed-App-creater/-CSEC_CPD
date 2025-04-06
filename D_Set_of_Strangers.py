t = int(input())  # Number of test cases

for _ in range(t):
    # Read n and m for the grid size
    n, m = map(int, input().split())
    
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    
    # Create two groups based on the checkerboard pattern (i + j) % 2
    group1 = []  # (i + j) % 2 == 0
    group2 = []  # (i + j) % 2 == 1
    
    # Fill the groups with colors based on positions
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                group1.append(grid[i][j])
            else:
                group2.append(grid[i][j])

    # Create dictionaries to count frequencies of each color in both groups
    count1 = {}
    count2 = {}
    
    for color in group1:
        if color in count1:
            count1[color] += 1
        else:
            count1[color] = 1
    
    for color in group2:
        if color in count2:
            count2[color] += 1
        else:
            count2[color] = 1
    
    # Sort counts to find the most frequent colors
    sorted1 = sorted(count1.items(), key=lambda x: -x[1])
    sorted2 = sorted(count2.items(), key=lambda x: -x[1])
    
    # Extract the best and second best colors for each group
    best1 = sorted1[0] if sorted1 else (None, 0)
    best2 = sorted2[0] if sorted2 else (None, 0)
    
    alt1 = sorted1[1] if len(sorted1) > 1 else (None, 0)
    alt2 = sorted2[1] if len(sorted2) > 1 else (None, 0)

    total1, total2 = len(group1), len(group2)
    
    # Try the best1 for group1 and best2 for group2
    if best1[0] != best2[0]:
        ans1 = (total1 - best1[1]) + (total2 - best2[1])
    else:
        ans1 = float('inf')

    # Try best1 for group1 and alt2 for group2
    ans2 = (total1 - best1[1]) + (total2 - alt2[1]) if alt2[0] is not None else float('inf')

    # Try alt1 for group1 and best2 for group2
    ans3 = (total1 - alt1[1]) + (total2 - best2[1]) if alt1[0] is not None else float('inf')

    # The result is the minimum of these strategies
    print(min(ans1, ans2, ans3))
