class Student:
    def __init__(self, physics, chem, math):
        self.physics = physics
        self.chem = chem
        self.math = math

    @property
    def pertan(self):
        return str((self.physics + self.chem + self.math) / 3) + "%"

stu1 = Student(80, 88, 93)
print(stu1.pertan)
stu1.physics=100
print(stu1.pertan)