for _ in range(int(input())):
	n=int(input())
	xor=0
	for i in range(1,n+1):
		l=list(map(int,input().split()))
		xor=xor^i
	print(xor)