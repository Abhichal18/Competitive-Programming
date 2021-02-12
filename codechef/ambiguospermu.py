t=int(input())
while(t!=0):
	lst=list(map(int,input().split()))
	inv=[0 for i in range(len(lst))]
	for i in range(len(lst)):
		inv[lst[i]-1]=i+1
	if(lst==inv):
		print("ambiguous")
	else:
		print("not ambiguous")
	t=int(input())