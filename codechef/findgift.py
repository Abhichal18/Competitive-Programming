for _ in range(int(input())):
	n=int(input())
	s=input()
	dict={'L':1,'R':1,'U':2,'D':2,'p':3}
	s='p'+s
	x=0
	y=0
	for i in range(1,n+1):
		if(s[i]!=s[i-1] and dict[s[i]]!=dict[s[i-1]]):
			if s[i]=='L':
				x=x-1
			elif s[i]=='R':
				x=x+1
			elif s[i]=='U':
				y=y+1
			elif s[i]=='D':
				y=y-1
	print(x,y)