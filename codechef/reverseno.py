T=int(input())
for t in range(T):
	n=int(input())
	lst=list()
	while(n>0):
		rem=n%10
		if(rem!=0):
			lst.append(rem)
		else:
			if(len(lst)!=0):
				lst.append(rem)
		n=n//10
	for i in range(len(lst)):
		print(lst[i],end="")
	print(end='\n')