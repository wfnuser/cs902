class linklist():
	def __init__(self, head = None, tail = None, cur = None):
		dic = {}
		dic['next'] = None
		dic['self'] = "head"
		self.cur = dic
		self.head = dic
		self.tail = dic
	
	def head(self):
		return self.head
	
	def tail(self):
		return self.tail
	
	def cur(self):
		return self.cur

	def append(self, val):
		dic = {}
		dic['self'] = val
		dic['next'] = None
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
		
	
	def listprint(self):
		self.cur = self.head

		while self.cur != None:
			print self.cur['self']
			self.cur = self.cur['next']


ll = linklist()

while(True):
	p = raw_input("please input name or q to quit\n")
	if p == "q" : break
	else : ll.insert(p)

ll.listprint()
