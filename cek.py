class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
    def average(self):
        return sum(self.grades)/ len(self. grades)
    

student = Student("Bob" (36, 67, 90, 100, 100))
print(student.average())