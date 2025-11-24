# Write Python program to **store student data in file using JSON
import json

# Create dictionary to store student data
student = {}

# Taking input from user
student["roll"] = int(input("Enter Roll Number: "))
student["name"] = input("Enter Student Name: ")
student["marks"] = float(input("Enter Marks: "))

# Convert dictionary to JSON and store in file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)   # indent → pretty formatting

print("Student data stored successfully in student.json")
