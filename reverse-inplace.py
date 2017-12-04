#To reverse a list
l=[1,2,3,4]
def rev(x):
	n=len(x)
	for i in range(int(n/2)):
		a=x[i]
		x[i]=x[n-(i+1)]
		x[n-(i+1)]=a
rev(l)
print(l)