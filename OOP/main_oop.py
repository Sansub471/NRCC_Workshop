class Student:
    def __init__(self, name:str, rollno:int, age:int, school:str) -> None:
        self.name = name
        self.rollno = rollno
        self.age = age
        self.school = school
    
    # controls what should be returned when the class object is represented
    # as a string
    def __str__(self) -> str:
        return f'{self.name}: {self.age}'

    def myname(self):
        return f'My name is {self.name}, {self.age} and still in college.'
    
std = Student('Subash', 45, 24, 'BESS')
print(std.name)
print(std)
print(std.myname())

# OOP with python is fun, but exam is here so let's stop it for the day.