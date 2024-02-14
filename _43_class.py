class Student:
    def __init__(self, name, age, math_score, literature_score):
        self.name = name
        self.age = age
        self.math_score = math_score
        self.literature_score = literature_score
        self.techer = "Dam Lan"
    
    def average_score(self):
        ave_score = (self.math_score + self.literature_score)/2
        return ave_score
    
    def print_info(self):
        print("Student name " + self.name + " study with " + self.techer + " have everage_score " + str(self.average_score())) 

students = []
s1 = Student("Lan", 21, 9, 8)
s2 = Student("Thinh", 21, 9, 7)
s3 = Student("Dam", 21, 9, 6)

students.append(s1)
students.append(s2)
students.append(s3)

for i in range(len(students)):
    students[i].print_info()






      
