for _ in range(int(input())):
	n=int(input())
	lst=list(map(int, input().split()))
	arr=[]
	for i in lst:
		if(i not in arr):
			arr.append(i)
	print(len(arr))