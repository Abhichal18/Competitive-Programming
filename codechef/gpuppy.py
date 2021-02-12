for t in range(int(input())):
	x,y=map(int, input().split())
	lst=list()
	for i in range(1,y+1):
		coins=x//i
		left=x-coins*i
		lst.append(left)
	print(max(lst))