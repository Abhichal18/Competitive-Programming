for _ in range(int(input())):
	n,k=map(int, input().split())
	sum=0
	time=0
	f=0
	for i in range(n):
		t,d=map(int, input().split())
		time+=t
		if(f==1):
			sum+=t*d
			continue
		if(time<=k):
			continue
		else:
			p=time-k
			sum+=p*d
			f=1
	print(sum)