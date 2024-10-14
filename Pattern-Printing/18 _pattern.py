def pattern1():
    for i in range(5, 0, -1):
        for j in range(i, 6):
            print(chr(64 + j), end=" ")
        print()

pattern1()
