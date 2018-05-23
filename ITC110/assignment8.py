# Create a Student class definition using the specifications.
class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []

    def name(self):
        return self.first_name + " " + self.last_name

    def addGrade(self, grade):
        self.grades.append(grade)


    def getGPA(self):
        return sum(self.grades) / len(self.grades)

# Test
sally = Student("Sally", "Supersmart")
sally.addGrade(4.0)
sally.addGrade(3.9)
sally.addGrade(4.0)
print(sally.grades)
# Prints
# [4.0, 3.9, 4.0]
print(sally.getGPA())
# Prints 3.97 (or 3.9666666666667)
print(sally.name())
# Prints "Sally Supersmart"
