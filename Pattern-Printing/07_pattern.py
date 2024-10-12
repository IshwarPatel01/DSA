n = 5  # Total number of lines

for i in range(1, n*2, 2):
    print(" " * ((n*2 - i) // 2) + "*" * i)




# n = 5

# for i in range(1, n+1):
#     print(" " * (n - i) + "*" * (2 * i - 1))




# n = 5

# for i in range(1, n+1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()
