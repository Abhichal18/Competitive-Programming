for _ in range(int(input())):
	n,k=map(int, input().split())
	lst=list(input().split())
	all=[]
	for i in range(k):
		lst1=list(input().split())
		all=all+lst1
	for i in lst:
		if(i in all):
			print("YES",end=" ")
		else:
			print("NO",end=" ")
	print()