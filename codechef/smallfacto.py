for t in range(int(input())):
	n=int(input())
	fact=1
	for i in range(1,n+1):
		if(n==1 or n==0):
			fact=fact*1
		else:
			fact=fact*i
	print(fact)