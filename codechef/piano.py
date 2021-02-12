for _ in range(int(input())):
	s=input()
	ans='yes'
	for i in range(len(s)):
		if i%2==0:
			if s[i]==s[i+1]:
				ans='no'
	print(ans)