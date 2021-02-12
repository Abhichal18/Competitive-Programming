for _ in range(int(input())):
	n=int(input())
	lst=list(map(int, input().split()))
	lst=sorted(lst,reverse=True)
	arr=[]
	f=0
	c=0
	for i in range(n):
		m=lst[0]
		pos=lst.index(m)
		if(lst.count(m)>=2):
			for j in range(2):
				lst.remove(lst[pos])
			arr.append(m)
			c+=1
		else:
			lst.remove(lst[pos])
		if(c==2):
			f=1
			break
	if(f==1):
		print(arr[0]*arr[1])
	else:
		print("-1")