for _ in range(int(input())):
	n,m=map(int, input().split())
	fruits=list(map(int, input().split()))
	price=list(map(int, input().split()))
	dict={}
	for i in range(len(fruits)):
		if(fruits[i] in range(1,m+1)):
			if(fruits[i] not in dict):
				dict[fruits[i]]=price[i]
			else:
				dict[fruits[i]]+=price[i]
	print(min(dict.values()))