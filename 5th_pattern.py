#Repeated Row Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(i): #runs i times.
        print(i, end=" ")
    print()