for _ in range(int(input())):
	n=int(input())
	lst=list(map(int, input().split()))
	count=0
	for i in range(n):
		m=1
		s=0
		for j in range(i,n):
			m=lst[j]*m
			s=lst[j]+s
			if(m==s):
				count+=1
	print(count)