a = input("Enter a number: ")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid input")

print("End of program")


#multiple error handling

a = input("Enter a number: ")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except ValueError:
    print("Invalid input")
except IndexError:  
    print("Index out of range")

#finally block

a = input("Enter a number: ")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except ValueError:
    print("Invalid input")
finally:
    print("End of program")     

#custom error handling
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

a = input("Enter a positive number: ")
try:
    num = int(a)
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    print(f"Multiplication table of {num} is:")
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
except ValueError:
    print("Invalid input: Please enter a valid integer.")
except NegativeNumberError as e:
    print(f"Custom Error: {e}")