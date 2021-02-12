for _ in range(int(input())):
	n=int(input())
	lst=list()
	for i in range(n):
		s1,s2=input().split()
		lst.append(s1)
		lst.append(s2)
	for i in range(0,2*n,2):
		if lst.count(lst[i])>1:
			print(lst[i],lst[i+1])
		else:
			print(lst[i])