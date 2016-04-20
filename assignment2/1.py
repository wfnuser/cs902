def main():
	f = raw_input("please input the number from:\n")
	t = raw_input("please input the number to:\n")
	i = raw_input("please input the increment:\n")

	for out in range(int(f),int(t),int(i)):
		print str(out)+", ",

main()
