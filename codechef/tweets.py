x,y=map(int, input().split())
dict={}
for _ in range(y):
	s=input()
	if(s!='CLOSEALL'):
		if(s in dict):
			if(dict[s]==0):
				dict[s]=1
			
			else:
				dict[s]=0
		else:
			dict[s]=1
	else:
		for i in dict:
			dict[i]=0
	print(sum(dict.values()))