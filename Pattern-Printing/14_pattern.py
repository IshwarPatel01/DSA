def print_alphabet_pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print(chr(65 + j), end="")
        print()  # Move to the next line

# Example usage
n = 5
print_alphabet_pattern(n)
