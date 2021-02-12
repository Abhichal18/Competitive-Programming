from math import *
for _ in range(int(input())):
	n=int(input())
	lst=list(map(int, input().split()))
	count=0
	for i in range(ceil(n/2)):
		if(lst[i]==lst[-1-i]):
			if(i!=0):
				if(lst[i]==lst[i-1] or lst[i]==lst[i-1]+1):
					count+=1
				else:
					break
			else:
				count+=1
	if(ceil(n/2)==count):
		print("yes")
	else:
		print("no")