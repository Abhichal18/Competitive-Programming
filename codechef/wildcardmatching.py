for _ in range(int(input())):
	x=input()
	y=input()
	flag=0
	for i in range(len(x)):
		if(x[i]==y[i] or x[i]=='?' or y[i]=='?'):
			flag=1
		else:
			flag=0
			break
	if(flag==1):
		print("Yes")
	else:
		print("No")