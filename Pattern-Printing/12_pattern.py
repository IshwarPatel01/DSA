

def print_pattern(n):
    for i in range(1, n+1):
        # Ascending part
        for j in range(1, i+1):
            print(j, end="")
        # Space between ascending and descending parts
        print(" " * (2 * (n - i)), end="")
        # Descending part
        for j in range(i, 0, -1):
            print(j, end="")
        print()  # Move to the next line

# Example usage
n = 4
print_pattern(n)
