s=input()
n=int(input())
for i in range(n):
	b=input()
	res="Yes"
	for  i in b:
		if(i in s):
			continue
		else:
			res="No"
			break
	print(res)