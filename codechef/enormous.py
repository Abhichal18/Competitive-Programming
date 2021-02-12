x,y=map(int, input().split())
count=0
for i in range(x):
	t=int(input())
	if(t%y==0):
		count=count+1
print(count)