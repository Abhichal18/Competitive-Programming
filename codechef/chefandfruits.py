for _ in range(int(input())):
	n,m,k=map(int, input().split())
	if(n==m):
		print('0')
	else:
		if(n>m):
			diff=n-m
			for i in range(1,k+1):
				m+=1
				dif=n-m
				if(dif<diff and dif>=0):
					diff=dif
			print(diff)
		else:
			diff=m-n
			for i in range(1,k+1):
				n+=1
				dif=m-n
				if(dif<diff and dif>=0):
					diff=dif
			print(diff)