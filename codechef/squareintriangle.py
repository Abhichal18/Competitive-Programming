for t in range(int(input())):
	n=int(input())
	if(n<4):
		print('0')
	else:
		val=n//2
		i=1
		count=0
		while(i<val):
			count=count+i
			i+=1
		print(count)