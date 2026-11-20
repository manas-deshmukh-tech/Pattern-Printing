#Hallow Square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1: #first row,last row,first column,last column
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()