import math
for _ in range(int(input())):
	n=int(input())
	c=0
	while(n!=0):
		y=int(math.sqrt(n))
		n=n-y*y
		c+=1
	print(c)