#Right-Aligned Triangle
n = 5
for i in range(1, n + 1):
    for j in range(n - i): #As rows increase, spaces decrease and stars increase, making the triangle right-aligned.
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()