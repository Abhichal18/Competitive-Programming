for _ in range(int(input())):
	s=input()
	k,x=map(int,input().split())
	dict={}
	for i in range(len(s)):
		if(s[i] not in dict):
			dict[s[i]]=1
		else:
			if(dict[s[i]]!=x):
				dict[s[i]]+=1
			else:
				if(k>0):
					k-=1
				else:
					break
	#print(dict)
	print(sum(dict.values()))