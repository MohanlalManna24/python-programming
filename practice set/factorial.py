# Factorial number::
num= int(input("Enter a Number: "))
if(num == 0 or num == 1):
    print(f"factorial of {num} = 1")
fact = 1    
for i in range(2,num+1):
    fact*=i
    
print(f"factorial of {num} = {fact}")    

#Factorial Using Recursion::
def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")