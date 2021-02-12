for _ in range(int(input())):
	x=int(input())
	if(x%10==0):
		print('0')
	elif(x%5!=0):
		print('-1')
	else:
		count=0
		while(x%10!=0):
			x=x*2
			count=count+1
		print(count)