def isprime(n):
	if(n==1):
		return False
	elif(n==2 or n==3):
		return True
	elif(n>=4):
		for i in range(2,n//2+1):
			if(n%i==0):
				return False
		return True
for _ in range(int(input())):
	x,y=map(int, input().split())
	# 1 added because atleast one harvested from 3rd field
	sum=x+y+1
	while(not isprime(sum)):
		sum+=1
	print(sum-x-y)