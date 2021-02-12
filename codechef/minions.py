for _ in range(int(input())):
	n,k=map(int, input().split())
	lst=list(map(int, input().split()))
	c=0
	for i in lst:
		i+=k
		if(i%7==0):
			c+=1
	print(c)