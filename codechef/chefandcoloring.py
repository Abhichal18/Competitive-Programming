for _ in range(int(input())):	
	n=int(input())
	s=input()
	dict={}
	for i in s:
		if(i not in dict):
			dict[i]=1
		else:
			dict[i]+=1
	m=max(dict.values())
	print(n-m)