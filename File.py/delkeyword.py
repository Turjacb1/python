class student:
    def __init__(self, name):
        self.name = name

s1 = student("turja")
del s1.name
print(s1.name)