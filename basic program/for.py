
# # multiplication table
N = int(input("Enter a number: "))
 
for i in range(1,11):
    print(f"{N} x {i} = {N * i}") 

# # greeting names starting with 'M'
l = ["Mohan", "Sohan", "Rohan", "John", "Doe", "Mica"]    
for i in l:
    if i.startswith("M"):
        print(f"Hello {i}, how are you?")


# check if a number is prime
num = int(input("Enter a number: "))
for i in range(2,num):
    if (num%i) == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")


# product of all numbers from 1 to n [factorial number]
n = int(input("Enter a number: "))
product =1
for i in range(2, n+1):
    product *= i
print(f"The product of all numbers from 1 to {n} is {product}")    

# sum of all numbers from 1 to n
sum=0
for i in range(1, n+1):
    sum+= i
print(f"The sum of all numbers from 1 to {n} is {sum}")
