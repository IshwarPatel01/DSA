# Number of rows for the pattern
n = 5  

# Print the alternating 1s and 0s pattern
for i in range(n):
    for j in range(i + 1):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()  # Move to the next line



