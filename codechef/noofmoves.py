for _ in range(int(input())):
	n=int(input())
	lst=list(map(int, input().split()))
	c=0
	s=sum(lst)
	print(s-n*min(lst))
	