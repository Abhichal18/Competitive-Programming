T=int(input())
for t in range(T):
	n=int(input())
	lst=list()
	while(n>0):
		rem=n%10
		lst.append(rem)
		n=n//10
	pos=len(lst)
	print(lst[0]+lst[pos-1])
	