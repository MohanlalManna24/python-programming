
1
12
123
1234
12345

# for i in range(6):
#     for j in range(1 , i + 1):
#         print(j, end=" ")
#     print()

1
23
456
78910
# num = 1
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#     print()    

# *
# **
# ***
# *****
# for i in range(6):
#     for j in range(1 , i + 1):
#         print("*", end=" ")
#     print() 


#      *
#     * *
#    * * *    

for i in range(1, 6):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()        