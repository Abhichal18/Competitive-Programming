for _ in range(int(input())):
	n,k=map(int, input().split())
	lst=list(map(int, input().split()))
	lst.sort()
	print(lst[(n+k)//2])