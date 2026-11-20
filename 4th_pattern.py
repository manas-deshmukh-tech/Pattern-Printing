#Increasing Number Triangle
n = 5
for i in range(1, n + 1): #controls the rows.
    for j in range(1, i + 1): #prints numbers from 1 to the current row number.
        print(j, end=" ")
    print()