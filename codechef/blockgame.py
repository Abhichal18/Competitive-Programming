for t in range(int(input())):
	n=input()
	k=''.join(reversed(n))
	if(n==k):
		print("wins")
	else:
		print("losses")
	