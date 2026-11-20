#Butterfly Pattern
n = 5
# Upper half
for i in range(1, n + 1): #stars increase and middle spaces decrease.
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)
# Lower half
for i in range(n, 0, -1): #stars decrease and middle spaces increase.
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)