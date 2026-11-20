#Star Pyramid
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1): #Each row increases by 2 stars (1, 3, 5, 7, 9).
        print("*", end="")
    print()