for _ in range(int(input())):
	n,m,k=map(int, input().split())
	ignored=list(map(int, input().split()))
	tracked=list(map(int, input().split()))
	count=0
	for i in ignored:
		if(i in tracked):
			count+=1
	count1=0
	for i in range(1,n+1):
		if(i not in tracked and i not in ignored):
			count1+=1
	print(count,count1)