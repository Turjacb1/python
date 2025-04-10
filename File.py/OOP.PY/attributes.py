class student:
  university="cstu"
  #default consturctor
  def __init__(self):
    pass
   


#parameterized consturctor
  def __init__(self,fullname,marks):
     self.name=fullname
     self.marks=marks
     print("adding  new name")

s1=student("turja",200)
print(s1.name)
print(s1.marks)
print(s1.university)

