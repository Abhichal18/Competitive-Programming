for _ in range(int(input())):
	lst=list(map(int, input().split()))
	flag=0
	for i in lst:
		if(lst.count(i)==2 or lst.count(i)==4):
			flag=1
		else:
			flag=0
			break
	if(flag==1):
		print("YES")
	else:
		print("NO")