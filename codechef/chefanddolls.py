for _ in range(int(input())):
	n=int(input())
	lst=list()
	for i in range(n):
		x=int(input())
		if(x in lst):
			lst.remove(x)
		else:
			lst.append(x)
	print(*lst)