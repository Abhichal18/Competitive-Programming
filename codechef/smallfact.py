T=int(input())
for t in range(T):
	n=int(input())
	fact=1
	for i in range(n):
		if(n==1 or n==0):
			fact=fact*1
		else:
			fact=fact*n
			n=n-1
	print(fact)