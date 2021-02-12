for _ in range(int(input())):
	n=int(input())
	lst=list(map(int, input().split()))
	arr=[]
	for i in lst:
		arr.append(lst.count(i))
	m=max(arr)
	print(len(lst)-m)