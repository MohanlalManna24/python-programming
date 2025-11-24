n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(" "*(n-i))
    print("*"*(2*i-1))