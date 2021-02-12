for t in range(int(input())):
	n=input().lower()
	l=len(n)
	if(l%2==0):
		x=sorted(n[0:l//2])
		y=sorted(n[l//2:l])
		if(x==y):
			print("YES")
		else:
			print("NO")
	else:
		x=sorted(n[0:(l//2)])
		y=sorted(n[l//2+1:l])
		if(x==y):
			print("YES")
		else:
			print("NO")