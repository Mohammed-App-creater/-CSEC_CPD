t = int(input())  # Read number of test cases

for _ in range(t):
    n = int(input())  # Read number of people
    if n == 1:  # If input is invalid (not in problem constraints)
        print(0)
        continue

    a = list(map(int, input().split()))  # Read their conditions
    a.sort()  # Sort the array in ascending order
    
    count = 0  # Tracks how many people are included
    result = 0  # Tracks the number of valid sets

    for i in range(n):
        if a[i] <= count:  # If the current person's requirement is satisfied
            result += 1  # We found a valid group
            count = 0  # Reset the count (new group can start)
        else:
            count += 1  # Increase count of selected people

    print(result)  # Print the number of valid ways
