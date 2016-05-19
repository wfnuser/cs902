import re

def main():
	inputfile = open("text.txt")
	output = open('data.txt','w')

	for line in inputfile:
#print line
		line = re.sub(r'[^A-z]\s*[0-9]{1,}\s{1}','',line)
		print line


main()
