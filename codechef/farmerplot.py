import math
for _ in range(int(input())):
	n,m=map(int,input().split())
	k=math.gcd(n,m)
	count1=0
	count2=0
	while(n>0):
		n=n-k
		count1+=1
	while(m>0):
		m=m-k
		count2+=1
	print(count1*count2)