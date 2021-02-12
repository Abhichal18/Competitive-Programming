import itertools
def minimal(s1,s2):
	count=0
	for i,j in zip(s1,s2):
		if(i!=j):
			if(i=='?' or j=='?'):
				count=count
			else:
				count=count+1
	return(count)
def maximal(s1,s2):
	count=0
	for i,j in zip(s1,s2):
		if(i!=j):
			if(i=='?' or j=='?'):
				count=count+1
			else:
				count=count+1
		else:
			if(i=='?' or j=='?'):
				count=count+1
	return(count)
for _ in range(int(input())):
	s1=input()
	s2=input()
	print(minimal(s1,s2), maximal(s1,s2))