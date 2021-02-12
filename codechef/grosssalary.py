for t in range(int(input())):
	n=int(input())
	if(n<1500):
		print(n+n*0.1+n*0.90)
	else:
		print(n+500+n*0.98)