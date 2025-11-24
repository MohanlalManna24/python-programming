#Write Python program to swap first and last element of list using function

def swap_first_last(lst):
    # Check list has at least 2 elements
    if len(lst) < 2:
        return lst
    
    # Swap first and last element
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Main program
numbers = [10, 20, 30, 40, 50]
print("Before swapping:", numbers)

numbers = swap_first_last(numbers)
print("After swapping:", numbers)
