def pattern_numbers():
    n = 4  # This represents the central number
    for i in range(n):
        for j in range(n):
            print(n - min(i, j), end="")
        for j in range(n-2, -1, -1):
            print(n - min(i, j), end="")
        print()
    
    for i in range(n-2, -1, -1):
        for j in range(n):
            print(n - min(i, j), end="")
        for j in range(n-2, -1, -1):
            print(n - min(i, j), end="")
        print()

pattern_numbers()
