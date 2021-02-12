for _ in range(int(input())):
	s=list(input())
	dict={}
	for i in s:
		if(i not in dict):
			dict[i]=1
		else:
			dict[i]+=1
	k=max(dict.values())
	if(len(s)-k==k):
		print("YES")
	else:
		print("NO")