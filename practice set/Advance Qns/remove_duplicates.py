def remove_duplicates(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

l= [10,15,75,45,45,1,2,3,1,4,5,2,3,6,7,8,5]
print(remove_duplicates(l))