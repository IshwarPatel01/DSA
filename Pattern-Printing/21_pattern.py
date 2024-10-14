def pattern2_fixed():
    n = 4
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)  # Print full stars for first and last rows
        else:
            print("*" + " " * (n - 2) + "*")  # Print stars with spaces in between

pattern2_fixed()
