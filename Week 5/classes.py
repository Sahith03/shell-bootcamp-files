#Using a class named Person
class Person:
    def __init__(self, name, age):
	self.name = name
	self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1)

#Using str fucntion
class Person:
    def __init__(self, name, age):
	self.name = name
	self.age = age
    def __str__(self):
	return f"{self.name}({self.age})" #f is float, which is used for conversion

p1 = Person("John", 36)

print(p1)


class Person:
    def __init__(self, name, age):
	self.name = name
	self.age = age

    def myfunc(self):
	print("Hello, my name is " + self.name+". Age is: "+str(self.age))

p1 = Person("John", 36)
p1.myfunc()

class Person:
    def __init__(myobj, name, age):
	myobj.name = name
	myobj.age = age

    def myfunc(abc):
	print("Hello, my name is " + abc.name+". Age is "+str(abc.age))

p1 = Person("John", 36)
p1.myfunc()







