class linklist():
	def __init__(self, head = None, tail = None, cur = None):
		dic = {}
		dic['next'] = None
		dic['self'] = "head"
		dic['before'] = None
		self.cur = dic
		self.head = dic
		self.tail = dic
	
	def head(self):
		return self.head
	
	def tail(self):
		return self.tail
	
	def cur(self):
		return self.cur

	def push(self, val):
		dic = {}
		dic['self'] = val
		dic['next'] = None
		dic['before'] = self.tail
		self.tail['next'] = dic
		self.tail = dic
	
	def insert(self, val):
		dic = {}
		dic['self'] = val

		pnt = self.head
		tmp = pnt['next']
		
		while(tmp != None and val >= tmp['self']):
			pnt = pnt['next']
			tmp = pnt['next']

		dic['next'] = tmp
		pnt['next'] = dic

	def isEmpty(self):
		if self.tail['self'] == "head":
				print "Empty"
		else:
				print "Not Empty"
		
	def pop(self):
		print self.tail['self']
		self.tail = self.tail['before']
	
	def listprint(self):
		self.cur = self.head

		while self.cur != None:
			print self.cur['self']
			self.cur = self.cur['next']


ll = linklist()

while(True):
	p = raw_input("please input name to push or q to quit or p to pop or e to check empty\n")
	if p == "q" : break
	if p == "p" : ll.pop()
	else : 
		if p == "e" : ll.isEmpty()
		else : ll.push(p)

ll.listprint()
