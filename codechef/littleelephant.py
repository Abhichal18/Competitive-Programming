for _ in range(int(input())):
	n,c=map(int, input().split())
	lst=list(map(int, input().split()))
	if(sum(lst)>c):
		print("No")
	else:
		print("Yes")