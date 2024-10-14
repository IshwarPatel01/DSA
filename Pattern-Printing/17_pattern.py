n = 5
for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Print increasing sequence of letters
    for j in range(i + 1):
        print(chr(65 + j), end="")
    # Print decreasing sequence of letters
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    print()
