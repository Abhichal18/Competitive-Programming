import math
for t in range(int(input())):
	n=int(input())
	lst=list()
	count=0
	x1,y1=map(int,input().split())
	x2,y2=map(int,input().split())
	x3,y3=map(int,input().split())
	d12=math.sqrt((x2-x1)**2+(y2-y1)**2)
	d23=math.sqrt((x3-x2)**2+(y3-y2)**2)
	d13=math.sqrt((x3-x1)**2+(y3-y1)**2)
	lst.append(d12)
	lst.append(d23)
	lst.append(d13)
	for i in lst:
		if(i>n):
			count=count+1
	if(count>1):
		print("no")
	else:
		print("yes")