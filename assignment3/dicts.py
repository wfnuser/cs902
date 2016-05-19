def main():
	n = input("input N to build a N*N dict\n")

	dict = {}

	for i in range(1,n+1):
		for j in range(1,n+1):
			dict[(i,j)] = 0
	
	while True:
		x = input("input x\n")
		y = input("input y\n")
		t = raw_input("input target num, if you just want to show the number, input s. if you want to leave input q\n")

		if(t == "s"):
			print dict[(x,y)]
			print "\n"
		else:
			if(t == "q"):
				break
			else:
				dict[(x,y)] = t

main()
