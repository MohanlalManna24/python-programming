s = input("Enter a string: ")
count = 0
vowels = "aeiou"
for char in s.lower():
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")