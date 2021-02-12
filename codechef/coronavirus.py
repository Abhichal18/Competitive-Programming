for _ in range(int(input())):
	n=int(input())
	lst=list(map(int, input().split()))
	lst.append(-10)
	c=1
	arr=list()
	for i in range(n):
		if(abs(lst[i+1]-lst[i])<=2):
			c+=1
		else:
			arr.append(c)
			c=1
	
	
	#print(arr)
	print(min(arr),max(arr))