
try:
    a = int(input("Hello, Enter a Number: "))
    print(a)
except Exception as e:
    print(e)
except ValueError as v:
    print(v)
except TypeError as t:
    print(t)    
print("Than You")        