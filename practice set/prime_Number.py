# Check the number is prime or not:: type 1
# num = int(input("Enter a number:"))
# counter = 0
# for i in range(1,num+1):
#     if num % i == 0:
#         counter = counter + 1
# if counter == 2:
#     print(f"{num} is a prime Number")
# else:
#     print(f"{num} is Not a prime Number")

#  ---------===========================================------------
# Check the number is prime or not:: type 2

# num = int(input("Enter a number: "))
# if num <= 1:
#     print(num, "is not a prime number")
# else:
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
    
#     if is_prime:
#         print(num, "is a prime number")
#     else:
#         print(num, "is not a prime number")
                
#  ---------===========================================------------
# print prime number up to 100   
             
print("Prime numbers up to 100:")

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

                       