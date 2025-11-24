# for n in range(1, 1000):
#     s = sum(int(d)**len(str(n)) for d in str(n))
#     if s == n:
#         print(n)

# for n in range(1, 1000):
#     d = str(n)
#     power = len(d)
#     total = sum(int(i)**power for i in d)
#     if total == n:
#         print(n)

#  ---------===========================================------------
        
# Check the number is Armstrong number or not
num = int(input("Enter a number: "))

sum_of_digits = 0
temp = num
power = len(str(num))   # count digits

while temp > 0:
    digit = temp % 10
    sum_of_digits += digit ** power 
    temp //= 10

if sum_of_digits == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
