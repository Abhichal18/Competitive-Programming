for t in range(int(input())):
	s=input()
	unprint=list()
	toprint=list()
	op=('+','/','^','-','*','(')
	for i in s:
		if(i in op):
			unprint.append(i)
		elif(i==')'):
			for j in range(len(unprint)-1,0,-1):
				if(unprint[j]=='('):
					unprint.pop()
					break
				else:
					toprint.append(unprint[j])
					unprint.pop()
		else:
			toprint.append(i)
	for i in toprint:
		print(i,end="")
	print()