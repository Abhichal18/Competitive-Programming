T=int(input())
lst=list()
for t in range(T):
	n=int(input())
	lst.append(n)
lst.sort()
for i in range(len(lst)):
	print(lst[i])