for _ in range(int(input())):
	n=int(input())
	lst=list(map(int, input().split()))
	while len(lst)!=2:
		l=[lst[0],lst[1],lst[2]]
		l.sort()
		mid=len(l)//2
		lst.remove(l[mid])
	print(*lst,end=' ')
	print()