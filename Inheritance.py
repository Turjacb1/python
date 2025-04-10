class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Turja", "Chakraborty")
x.printname()
