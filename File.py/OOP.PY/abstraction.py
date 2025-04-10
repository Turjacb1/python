class car:
    def __init__(self):
        self.acc = False
        self.brek = False
        self.cluc = False

    def start(self):
        self.acc = True
        self.cluc = True
        print("car started")

car1 = car()
car1.start()