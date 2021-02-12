T=int(input())
for t in range(T):
	lst=list()
	x,y,z=map(int, input().split())
	lst.append(x)
	lst.append(y)
	lst.append(z)
	lst.sort()
	print(lst[1])