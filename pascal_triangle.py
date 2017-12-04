n=int(input("Give the number of rows"))
for i in range(1,n+1):
	for j in range(1,n+1-i):
		print(" ",end="")
	a=11**(i-1)
	a=str(a)
	l=[]
	for k in range(0,i):
		l.append(a[k])
		print(l[k],end=" ")
	print()
	