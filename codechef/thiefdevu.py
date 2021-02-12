for _ in range(int(input())):
	m,x,y=map(int,input().split())
	lst=list(map(int, input().split()))
	houses=[0]*100
	max=x*y
	for i in lst:
		upper=i+max
		lower=i-max
		if(lower<1):
			lower=1
		if(upper>100):
			upper=100
		for j in range(lower, upper+1):
			if(houses[j-1]==0):
				houses[j-1]=1
	print(houses.count(0))