for t in range(int(input())):
	x,y=map(int, input().split())
	for i in range(x):
		y=(y*(y+1)//2)
	print(y)