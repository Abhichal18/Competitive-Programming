for _ in range(int(input())):
	x,y,k,n=map(int, input().split())
	req=x-y
	flag=0
	for i in range(n):
		p,c=map(int,input().split())
		if(req<=p and c<=k):
			flag=1
	if(flag==0):
		print("UnluckyChef")
	else:
		print("Luckychef")