for _ in range(int(input())):
	x,y,k=map(int, input().split())
	#fin total score 
	total_score=x+y
	#find how many services are done yet
	service_changed_yet=total_score//k
	#if service yet are even then next service of chef else paja
	if(service_changed_yet%2==0):
		print("Chef")
	else:
		print("Paja")