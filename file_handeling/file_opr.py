import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "file.txt")

# f = open(file_path)
# data = f.read()
# print(data)
# f.close()

# or
 #with open("file.txt") as f:
 #   print(f.read())

# =================================

str = "Hello everyone!, This is a python programming."
a = open("myfile.txt","w")
a.write(str)
a.close()
