txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)


txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)


txt = "banana"
x = txt.center(20)
print(x)


txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


txt = "My name is Ståle"
x = txt.encode()
print(x)


txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)



txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)



txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


txt = "Company12"
x = txt.isalnum()
print(x)


txt = "1234"
x = txt.isdecimal()
print(x)


txt = "hello world!"
x = txt.islower()
print(x)



txt = "   "
x = txt.isspace()
print(x)


txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")


txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)


txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)


txt = "Hello, welcome to my world."
x= txt.startswith("Hello")
print(x)


txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")



txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)



txt = "Welcome to my world"
x = txt.title()
print(x)



#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {73:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


txt = "50"
x = txt.zfill(10)
print(x)