# ----------------------------
# function
def myFunc(arg1, arg2):
	return arg1 + arg2
	
print(myFunc(2, 3))

# ----------------------------
# lambda experssion
# def square(num):
#	return num**2 
square = lambda num: num**2
even = lambda x: x%2==0

print(square(2))
print(even(9))

# ----------------------------
# clasic vs new-style class

# In Python2 
# In Python2 it is a good idea to make all classes new-style classes
class Classic(object):
	pass

print(dir(Classic))

# In Python3 all classes are new-style classes
class NewClass():
	pass

print(dir(NewClass))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

# ----------------------------
# OOP
# Circle => class Name upper case
# the Circle class is extending a class called object
# object is the mother of all classes in Python


class Circle(object):
	# class object attributes
	pi = 3.14
	
	def __init__(self, radius = 1):
		self.radius = radius
		
	def area(self):
		print(Circle.pi)
		return self.radius**2*Circle.pi
		
	# method to reset radius
	def setRadius(self, radius):
		self.radius = radius
	
	# method for getting radius
	# same as just calling radius
	def getRadius(self):
		return self.radius
		
# create an instance
myCircle = Circle()
print(myCircle.radius)
print(myCircle.pi)

myCircle.setRadius(2)
print(myCircle.radius)
print(myCircle.area())

# ----------------------------
# OOP Inheritance

class Animal():
	
	def __init__(self):
		print("An animal is borned")
		
	def whoAmI(self):
		print("I'm an animal")
		
	def eat(self):
		print("I eat")

# Dod inherit from Animal		
class Dog(Animal):
	
	def __init__(self):
		Animal.__init__(self)
		print("It is a dod")
		
	def whoAmI(self):
		print("I'm a dog")
	
	def bark(self):
		print("woof")
		
medor = Dog()
medor.bark()

# ----------------------------
# special methods ?

# __init__
# __str__
# __len__
# __del__
