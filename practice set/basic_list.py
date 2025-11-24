l= [1,2,5,4,62,1,5,45,12,45,51,32,14,25,36,47,58,69,70]
# Print the original list
print("Original list:", l)

# Sort the list in ascending order
l.sort()
print("Sorted list:", l)
# Reverse the list
l.reverse()
print("Reversed list:", l)
# Print the length of the list
print("Length of the list:", len(l))
# Print the maximum and minimum values in the list
print("Maximum value:", max(l))
print("Minimum value:", min(l))
# Print the sum of all elements in the list
print("Sum of all elements:", sum(l))
# Print the average of the elements in the list
print("Average of elements:", sum(l)/len(l))
# Print the first and last elements of the list
print("First element:", l[0])
print("Last element:", l[-1])
# Print the elements at even and odd indices
print("Elements at even indices:", l[0::2])
print("Elements at odd indices:", l[1::2])
# Print the list sliced from index 2 to 8
print("Sliced list (index 2 to 8):", l[2:9])
# Print the list in chunks of 5 elements
print("List in chunks of 5 elements:")
for i in range(0, len(l), 5):
    print(l[i:i+5])
# Check if a specific value (e.g., 25) is in the list
value_to_check = 25
print(f"Is {value_to_check} in the list?", value_to_check in l)
# Count the occurrences of a specific value (e.g., 45) in the list
value_to_count = 45
print(f"Occurrences of {value_to_count} in the list:", l.count(value_to_count))
# Find the index of a specific value (e.g., 62) in the list
value_to_find = 62
if value_to_find in l:
    print(f"Index of {value_to_find} in the list:", l.index(value_to_find))
else:
    print(f"{value_to_find} is not in the list")
# Add a new value (e.g., 100) to the end of the list
l.append(100)
print("List after adding 100:", l)
# Remove a specific value (e.g., 1) from the list
l.remove(1)
print("List after removing 1:", l)
# Clear the entire list
l.clear()
print("List after clearing all elements:", l)
