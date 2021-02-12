T=int(input())
menu=(2048,1024,512,256,128,64,32,16,8,4,2,1)
for t in range(T):
	n=int(input())
	count=0
	for i in menu:
		while(n>=i):
			count=count+n//i
			n=n%i
	print(count)		