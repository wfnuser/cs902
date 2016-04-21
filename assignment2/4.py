def main():
	start = input("the start number:")
	end   = input("the end number:")
	
	bits = 0
	tmp  = end
	strs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	hex  = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

	while tmp!=0:
		tmp = tmp/2
		bits = bits + 1

	if(end >= 33):
		flag = 1
	else: flag = 0

	print "DEC     ",
	print "BIN     ",
	print "OCT     ",
	print "HEX     ",

	if(flag): print "ASCII   "
	else: print ""

	for i in range(start,end+1,1):
		print "%2d"%i,
		print "     ",

		tmp = i
		pos = bits

		str2 = ""

		while tmp!=0:
			if(tmp%2==1): strs[pos] = 1
			else:         strs[pos] = 0
			tmp = tmp/2
			pos = pos - 1

		for j in range(1,pos+1):
			strs[j] = 0

		for j in range(1,bits+1):
			str2 = str2 + '%d'%strs[j]

		print str2.ljust(8),

			
		tmp = i
		pos = bits/3 + 1

		str2 = ""

		while tmp!=0:
			strs[pos] = tmp%8
			tmp = tmp/8
			pos = pos - 1

		for j in range(1,pos+1):
			strs[j] = 0

		for j in range(1,bits/3+1+1):
			str2 = str2 + '%d'%strs[j]

		print str2.ljust(8),

			
		tmp = i
		pos = bits/4 + 1

		str2 = ""

		while tmp!=0:
			strs[pos] = tmp%16
			tmp = tmp/16
			pos = pos - 1

		for j in range(1,pos+1):
			strs[j] = 0

		for j in range(1,bits/4+1+1):
			str2 = str2 + hex[strs[j]]

		print str2.ljust(8),

		if(flag and i>=33): print chr(i)
		else: print ""

			
main()		
