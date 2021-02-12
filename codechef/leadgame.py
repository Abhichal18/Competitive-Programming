T=int(input())
l1=list()
l2=list()
mx=0
p1=0
p2=0
for t in range(T):
	x,y=map(int, input().split())
	p1=p1+x
	p2=p2+y
	if(p1>p2):
		lead=p1-p2
		l1.append(lead)
		if(lead>mx):
			mx=lead
	else:
		lead=p2-p1
		l2.append(lead)
		if(lead>mx):
			mx=lead
if mx in l1:
	print("1",mx)
else:
	print("2",mx)