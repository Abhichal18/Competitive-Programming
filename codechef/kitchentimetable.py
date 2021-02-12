for _ in range(int(input())):
	n=int(input())
	schedule=list(map(int, input().split()))
	cook=list(map(int, input().split()))
	count=0
	for i in range(n):
		if(i==0):
			if(schedule[i]-0>=cook[i]):
				count+=1
		else:
			if(schedule[i]-schedule[i-1]>=cook[i]):
				count+=1
	print(count)