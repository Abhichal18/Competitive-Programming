for _ in range(int(input())):
	n=int(input())
	lst=list(map(int, input().split()))
	lst.sort()
	print((n-1)*lst[0])