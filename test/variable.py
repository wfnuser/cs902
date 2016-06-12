x = 12
def f():
	global x
	x = x+1

f()
print(x)

def headtail(list):
	          return list[0], list[len(list)-1]
h = headtail([1,2,3])
print(h)

def MySecondFunction(name="Jess", score=99):
	       print "%s -> %d" % (name, score)

MySecondFunction(1)
