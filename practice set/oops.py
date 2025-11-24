
# Examples::1

# class students:
#     def __init__(self,name, marks):
#         self.name = name
#         self.marks= marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "Your average score is: ", sum/3)        
        
# s1 = students("mohanlal",[100,80,60])
# s2 = students("mohanlal",[10,80,60])
# s3 = students("mohanlal",[100,50,60])
# s1.get_avg()        
# s2.get_avg()        
# s3.get_avg()        


# Examples::2  

# class Account:
#     def __init__(self,bal, acc):
#         self.balance = bal
#         self.account = acc
        
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was dedited")   
#         print("total balance =", self.get_balance())     
        
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")   
#         print("total balance =", self.get_balance()) 
    
#     def get_balance(self):
#         return self.balance
    
    
# acc1 = Account(10000, 12345)
# acc1.debit(int(input("which amount you went to Debit:")))
# acc1.credit(5000)


# Examples::3 == single inheritance

# class car:
#     def start():
#         print("car starting")
    
#     def stop():
#         print("Car Stopped")    
 
# class ToyotaCar(car):
#     def __init__(self, brand):
#         self.brand = brand

# ToyotaCar.start()


# Examples::3 == multiple inheritance

class A:
    varA = "Welcame to var A"
    
class B:
    varB = "Welcame to var B"
    
class C(A,B):
    varC = "Welcame to var C" 

c1 = C()
print(c1.varC)           
print(c1.varB)           
print(c1.varA)


# Examples::3 == 


           