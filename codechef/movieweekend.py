for _ in range(int(input())):
	n=int(input())
	l=list(map(int, input().split()))
	r=list(map(int, input().split()))
	arr=[]
	for i in range(n):
		arr.append(l[i]*r[i])
	m=max(arr)
	pos=-1
	if(arr.count(m)>1):
		k=max(r)
		if(r.count(k)>1):
			pos=r.index(k)
		else:
			pos=r.index(k)
	else:
		pos=arr.index(m)
	print(pos+1)