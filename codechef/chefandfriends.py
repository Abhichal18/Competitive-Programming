n=int(input())
c=0
lst=['ch','he','ef','che','hef','chef']
for _ in range(n):
	u=input()
	for i in lst:
		if i in u:
			c+=1
			break
print(c)