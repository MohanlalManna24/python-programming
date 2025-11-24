def ractorial(n):
    if(n==1 or n==0):
        return 1
    return n * ractorial(n-1)

n = int(input("Enter a number: "))
print("The factorial of", n, "is:", ractorial(n))
