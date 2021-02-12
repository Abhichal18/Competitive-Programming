for _ in range(int(input())):
	n=int(input())
	lst=list()
	for j in range(n):
		lst1=list(map(int, input().split()))
		lst.append(lst1)
	for i in range(n-1,0,-1):
		for j in range(i):
			lst[i-1][j]+=max(lst[i][j],lst[i][j+1])
	print(lst[0][0])