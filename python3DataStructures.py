# Python3 cheatSheet

# Python2 vs Python3

# classic divison / true division
# to inport division in Python2
# from __future__ import division 

# print is a statement / print is a function


# ---------------------------------
# Import

# from math import ceil
# num = ceil(2.8)
# print(num)

# or

import math
num = math.ceil(2.8)
print(num)

# function in module math
print(dir(math))

# print help
help(math.ceil)

# ---------------------------------
# Numbers
a = -1.2 #float
b = 2 	# int
c = a + b 
print(c) 

c = 0
print(c) 

# powers **
print(2**3)

#true division
print(10/3)
# 3.3333333

# modulo
print(10%3)

# ---------------------------------
# Strings 
# IMMUTABILITY (But can append)
s = "hello"

# slicing
print(s[1:]) #ello
print(s[:3]) #hel
print(s[-1]) #o 
print(s[:-1]) #hell 
print(s[::-1]) #olleh

# format
s = 'toto et {}'.format('titi')
print(s)

s = '{a} et {b}'.format(a='toto', b='titi')
print(s)

# ---------------------------------
# Lists
myList = [1, 2, 3, 'a', 2.3, 'toto']

myList.append('gui')
print(myList)

myList.pop()
print(myList)

myList.reverse()
print(myList)

myList = [1, 2, 3, 0]
myList.sort() # not supported if str and float ot int
print(myList)

# list comprehension
lst = [x for x in 'hello']
print(lst) # ['h', 'e', 'l', 'l', 'o']

lst = [x for x in range(11) if x % 2 == 0]
print(lst) # [0, 2, 4, 6, 8, 10]

# ---------------------------------
# Dictionnaries
myDict = {'key':'value', 'name':'guillaume', 'age':34}
print(myDict)

# add a key
myDict['address'] = 'Cupertino'
print(myDict)

# get keys ['key', 'name', 'age', 'address']
keysList = myDict.keys()
print(keysList)

# get values ['value', 'guillaume', 34, 'Cupertino']
valuesList = myDict.values()
print(valuesList)

# get tuples [('key', 'value'), ('name', 'guillaume'), ('age', 34), ('address', 'Cupertino')]
itemsTuple = myDict.items()
print(itemsTuple)

# ---------------------------------
# Tuples
# IMMUTABILITY

myTuple = ('guillaume', 'chou', 34)
print(myTuple)

# ---------------------------------
# Sets
# unordered collection of unique element
mySet = {1, 2, 3}
print(mySet)
myList = [1, 2, 4, 4, 1]

# cast a list to a set 
mySet = set(myList)
print(mySet)

# ---------------------------------
# Booleans
a = True
b = False

print(a and b)
print(a or b)

# ---------------------------------
# Statements

a = 2 
b = 2

# if else elif
if (a > b):
	print ('a is above b')
elif (a < b): 
	print ('a is under b')
else:
	print ('a equal b')
	
# ---------------------------------
# for loop
l = [1, 2, 3]
for num in l:
	print(num)
	
d = {'k1':1, 'k2':2, 'k3':3}
for key in d:
	print(key,':',d[key])
	print('{}:{}'.format(key,d[key]))
	
for k,v in d.items():
	print(k,v)

# ---------------------------------
# while loop
x = 0
while x < 10:
	print(x)
	x += 1

# break => break out of the current closest enclosing loop
# continue => goes to the top of the closest enclosing loop
# pass => does nothing

# ---------------------------------
# Ranges
for num in range(10):
	print(num)












