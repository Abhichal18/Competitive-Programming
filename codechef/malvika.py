for _ in range(int(input())):
	s=input()
	lst=list(s)
	if(lst.count('a')>lst.count('b')):
		print(lst.count('b'))
	else:
		print(lst.count('a'))