n=int(input())
for i in range(n):
	lst=list(map(int, input().split()))
	if(lst.count(1)==0):
		print("Beginner")
	elif(lst.count(1)==1):
		print("Junior Developer")
	elif(lst.count(1)==2):
		print("Middle Developer")
	elif(lst.count(1)==3):
		print("Senior Developer")
	elif(lst.count(1)==4):
		print("Hacker")
	else:
		print("Jeff Dean")