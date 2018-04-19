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
# OOP
# Circle upper case

class Circle(object):
	# class object attributes
	pi = 3.14
	
	def __init__(self, radius = 1):
		self.radius = radius
		
	def area(self):
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

myCircle.setRadius(2)

