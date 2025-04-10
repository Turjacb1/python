class A:
    vara="welcome to A"
class B:
    varb="welcome to B"
class C(A,B):
    varc="welcome to c"
c1=C()
print(c1.vara)
print(c1.varb)
print(c1.varc)
    