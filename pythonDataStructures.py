from __future__ import division
#from __future__ import print_function

# classic divison
print(10/3)
# 3 if from __future__ import division commented out

print("Hello")
# print "Hello" doesn't work because of from __future__ import print_function

# print fornatting
s = 'guillaume'
print 'bonjour %s' %(s)

# use of iteritems in Pyhton2 instead of items
d = {'k1':1, 'k2':2, 'k3':3}
	
for k,v in d.iteritems():
	print k
	print v
	
# use xrange instead of range
for num in xrange(10):
	print(num)



