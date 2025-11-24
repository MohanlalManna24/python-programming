class student:
    college_name = "GGI College"
    
    @staticmethod
    def welcome_note():
        print("Welcome to", student.college_name)
        
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Student Object Created")
        
s1 = student("mohanlal",98) 
print(f"{s1.welcome_note()} Student Name: {s1.name} Marks: {s1.marks}")       