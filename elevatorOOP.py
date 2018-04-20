# https://discuss.leetcode.com/topic/94696/design-an-elevator-system
class Elevator():
	
	def __init__(self, currentLevel = 0, minLevel = -2, maxLevel = 10):
		#self.callQueue = []	
		#self.levelQueue = []
		self.currentLevel = currentLevel
		self.minLevel = minLevel
		self.maxLevel = maxLevel
		# 0 ground floor
		self.doorOpen = False 
		print('Elevator waiting at level ' + str(self.currentLevel))
	
	def toogleDoor(self):
		self.doorOpen = not self.doorOpen
		if self.doorOpen:
			print("door opening")
		else:
			print("door closing")
		
	def move(self, up, level):
		self.toogleDoor()
		start = self.currentLevel
		if start < level:
			print("going up")
			for num in range(start, level + 1):
				self.currentLevel = num
				print('level #' + str(num))
		else:
			print("going down")
			for num in range(start, level-1, -1):
				self.currentLevel = num
				print('level #' + str(num))
		self.toogleDoor()
		
	def call(self, level, up):
		# int level = where is the guy calling the Elevator
		# bool up = true if the guy want to go up or flase if down
		if up:
			print('call from level ' + str(level) + ' to go up')
		else:
			print('call from level ' + str(level) + ' to go down')
		
		if level > self.currentLevel:
			#self.toogleDoor()
			self.move(True, level)
		elif level < self.currentLevel:
			#self.toogleDoor()
			self.move(False, level)
		else:
			self.toogleDoor()
		
	def level(self, level):
		print('user want to go to level ' + str(level))
		
		if self.currentLevel < level:
			#self.toogleDoor()
			self.move(True, level)
			#self.toogleDoor()
		elif self.currentLevel > level:
			#self.toogleDoor()
			self.move(False, level)
			#self.toogleDoor()
		# else:
			# door stay open
		
myElevator = Elevator()

# call from user at level 0 
# user want to go up
myElevator.call(0, True)	
# user press button 10 to go up
myElevator.level(10)

# in the mean time 
# a user is calling from level 5 to go up
myElevator.call(5, True)
myElevator.level(7)

myElevator.call(8, False)
myElevator.level(0)
