class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total balance:", self.getbalance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance:", self.getbalance())

    def getbalance(self):
        return self.balance

acc1 = Account(4000, 1234)
acc1.debit(2000)
acc1.credit(500)
