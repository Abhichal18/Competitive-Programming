for _ in range(int(input())):
	c,d,l=map(int, input().split())
	if(c<=2*d):
		if((d*4)<=l and l%4==0 and ((d+c)*4)>=l):
			print("yes")
		else:
			print("no")
	else:
		extra=c-2*d
		if(((d*4)+(extra*4))<=l and l%4==0 and l<=((d+c)*4)):
			print("yes")
		else:
			print("no")