class Student:
    def __init__(self, name:str, rollno:int, age:int, school:str) -> None:
        self.name = name
        self.rollno = rollno
        self.age = age
        self.school = school

std = Student('Subash', 45, 24, 'BESS')
print(std.name)