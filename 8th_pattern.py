#Inverted Star Pyramid
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1): #Stars decrease by 2 in each row, making an inverted pyramid.
        print("*", end="")
    print()