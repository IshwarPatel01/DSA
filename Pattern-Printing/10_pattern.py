# Total number of rows for the pattern
n = 5  

# Print the star pattern
for i in range(1, n + 1):
    print("*" * i)  # Increasing stars

for i in range(n, 0, -1):
    print("*" * i)  # Decreasing stars
