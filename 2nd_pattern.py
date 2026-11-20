#Right Angle Triangle
n = 5
for i in range(1,n + 1): #control row
    for j in range(i): #prints stars equal to current row no
        print("*", end=" ")
    print() ##moves to next line after each row