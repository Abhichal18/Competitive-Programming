for _ in range(int(input())):
	n=int(input())
	a=list(map(int, input().split()))
	b=list(map(int, input().split()))
	a_max=max(a)
	b_max=max(b)
	a_total=sum(a)-a_max
	b_total=sum(b)-b_max
	if(a_total<b_total):
		print("Alice")
	elif b_total<a_total:
		print('Bob')
	else:
		print('Draw')