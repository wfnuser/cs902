
days = [31,28,31,30,31,30,31,31,30,31,30,31]
mons = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
wees = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

strs = []

def is_leap(year):
	if (year%4==0 and (year%100!=0 or year%400==0)) :
		return True
	else :
		return False


def main():
	year = input("please input the year you want to get: ")
	isleap = is_leap(year) and 1 or 0	

	first_day = (365*(year-1900)+((year-1900-1)/4+1)-((year-1900-1)/100+1)+(year-1600-1)/400)%7

	print "The Calendar of %d"%year
	print first_day
	
	for i in range(0,12):
		strs.append([])	

	for index,mon in enumerate(mons):
		print "\n"
		print mon
		for week in wees:
			print week+"  ",
		print ""

		day_sum = days[index]
		if (is_leap(year) and index == 1): day_sum = day_sum+1 
	
		for i in range(0,first_day):
			print "     ",
			strs[index].append("     ")
	
		
		for i in range(1,day_sum+1):
			print "%2d   "%i,
			strs[index].append("%2d   "%i)
			if((first_day+i)%7 == 0):
				print"\n",
		
		for i in range(day_sum+first_day,42):
			strs[index].append("     ")


		if(first_day == 0):
			print""
		
		first_day = (day_sum + first_day) % 7
		
	for index in range(0,4):
		print "\n"
		for i in range(0,3):
			print mons[index*3+i],
			print "  ",
			for j in range(0,7):
				print "    ",
		print ""		

		for i in range(0,3):
			for week in wees:
				print week+"  ",

		print ""		
		
		for row in range(0,6):
			for i in range(0,3):
				for j in range(0,7):
					print strs[index*3+i][j+row*7],

			print ""
				
main()
		
			
	
