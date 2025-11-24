s1 = int(input("Enter first side: "))
s2 = int(input("Enter second side: "))
s3 = int(input("Enter third side: "))
if s1 == s2 == s3:
     print("Equilateral triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
     print("Isosceles triangle")
else:
     print("Scalene triangle")