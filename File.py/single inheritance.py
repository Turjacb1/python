class car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")

        class BMW(car):#instance method
                 def __init__(self,name):
                  self.name=name

car1=BMW("pajero")
car2=BMW("lamboroghini")
print(car1.start())

              