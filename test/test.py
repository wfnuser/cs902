def perm(list,k,m):
	if k == m:
		for i in range(m):
			print list[i],
		print
	else:
		for i in range(k,m):
			list[k],list[i] = list[i],list[k]
			perm(list,k+1,m)
			list[k],list[i] = list[i],list[k]

myList = [1,2,3]
perm(myList,0,3)
