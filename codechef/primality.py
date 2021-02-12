for t in range(int(input())):
	n=int(input())
	flag=0
	if(n==1):
		flag=0
	elif(n==2 or n==3):
		flag=1
	else:
		for i in range(2,n//2+1):
			if(n%i==0):
				flag=0
				k=i
				break
			else:
				flag=1
	if(flag==0):
		print("no",i)
	else:
		print("yes")