s = {2,3,5,3}
print(s)    # Output: {2, 3, 5}

s1 = {1,2,5}
s2 = {1,3,4,5,6,7}
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5, 6, 7}
s1.update(s2)  # s1 now contains all elements from both sets
print(s1 , s2)  # Output: {1, 2, 3, 4, 5, 6, 7}


