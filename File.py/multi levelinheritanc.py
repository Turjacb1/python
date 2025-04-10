class car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")

        class BMW(car):
            def __init__(self,brand):
                self.name=brand


        class fortuner(BMW):
            def __init__(sekftype):
              
              car1=fortuner("petrol")
              print(car1.start)
