T=int(input())
for t in range(T):
	n=int(input())
	lst=list()
	while(n>0):
		rem=n%10
		if(rem==4):
			lst.append(rem)
		n=n//10
	print(len(lst))