c=(100,50,10,5,2,1)
for t in range(int(input())):
	n=int(input())
	count=0
	for i in c:
		while(n>=i):
			count=count+n//i
			n=n%i
		
	print(count)