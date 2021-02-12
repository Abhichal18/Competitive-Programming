for _ in range(int(input())):
	a,b=map(int, input().split())
	j=1
	flag=0
	while True:
		if(j%2!=0):
			a-=j
			j+=1
			flag=1
			if(b<j):
				break
		else:
			b-=j
			j+=1
			flag=2
			if(a<j):
				break
	if(flag==1):
		print("Limak")
	else:
		print("Bob")