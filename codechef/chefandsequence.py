for _ in range(int(input())):
	l=int(input())
	lst=list(map(int, input().split()))
	f=int(input())
	arr=list(map(int, input().split()))
	ans="Yes"
	for i in arr:
		if(i in lst):
			continue
		else:
			ans="No"
			break
	print(ans)