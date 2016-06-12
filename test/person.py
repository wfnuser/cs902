class Person:
	def __init__(self,n,y):
		self.name = n
		self.year = y
	
	def whatName(self):
		print self.name

p = Person('mark',1994)
p.whatName()
