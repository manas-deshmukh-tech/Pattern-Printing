#Hollow Right-Angled Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == 1 or i == n or j == 1 or j == i: #first row,last row (prints full stars),first column (left boundary),diagonal boundary.
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()