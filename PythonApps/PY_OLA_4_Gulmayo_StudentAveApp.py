class Student:
    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english
    def compute_average(self):
        self.average = (self.math + self.science + self.english) / 3
    def display_info(self):

        self.compute_average()
        if self.average >= 75:
            status = "Passed"
        else:
            status = "Failed"

        print(f"Name: {self.name}")
        print(f"Math: {self.math}")
        print(f"Science: {self.science}")
        print(f"English: {self.english}")
        print(f"Average: {self.average:.2f} ({status})")


print("Gulmayo, Shayne Marie F.")
print("3BSIT-1\n")

name = input("Enter Student's Name: ")
math = float(input("Enter Math Grade: "))
science = float(input("Enter Science Grade: "))
english = float(input("Enter English Grade: "))

student = Student(name, math, science, english)

student.display_info()