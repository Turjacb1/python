class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopted")
class bmw(car):
          def __init__(self,name,type):
            self.name=name
            super().__init__(type)
            super().start()

car1=bmw("pajero","electroc")
print(car1.type)

            
