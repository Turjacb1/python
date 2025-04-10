class student:
    # parameterized constructor
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("adding new name")

    def A(self):
        print("millionaire")

    def getmarks(self):  # Corrected indentation
        return self.marks

s1 = student("turja", 200)

s1.A()
print(s1.getmarks())
        

        