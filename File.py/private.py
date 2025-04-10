class account:
    def __init__(self, accno, accpass):
        self.accno = accno
        self.__accpass = accpass

    def get_accpass(self):
        return self.__accpass

acc1 = account("1234", "abcd")

print(acc1.accno)

# Accessing the private attribute using a method
print(acc1.get_accpass())
      