for t in range(int(input())):
	q,p=map(int,input().split())
	pr=p*q
	if(q>1000):
		prd=q*p*0.1
		pr=pr-prd
		print("%.6f"%pr)
	else:
		print("%.6f"%pr)