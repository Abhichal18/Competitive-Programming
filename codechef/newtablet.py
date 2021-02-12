for _ in range(int(input())):
	n,b=map(int,input().split())
	max=-1
	for i in range(n):
		w,h,p=map(int, input().split())
		if p<=b:
			area=w*h
			if(area>max):
				max=area
	if(max==-1):
		print("no tablet")
	else:
		print(max)