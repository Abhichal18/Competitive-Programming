for _ in range(int(input())):
	n=int(input())
	dict={}
	for i in range(n):
		p,s=map(int, input().split())
		if p in dict:
			if dict[p]<s:
				dict[p]=s
		elif p not in dict and p<9:
			dict[p]=s
	print(sum(dict.values()))