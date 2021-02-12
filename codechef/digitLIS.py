for _ in range(int(input())):
	n=int(input())
	lst=list(map(int, input().split()))
	s=""
	for i in lst:
		s+=str(i)
	print(s)