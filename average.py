# finding average
n=[['Bob', 56, 80, 72, 90],['Alice', 60, 88, 44, 70]]
l=[]
def avg(x):
	for i in x:
		sum=0
		for j in range(len(i)-1):
			sum=sum+int(i[j+1])
		l.append([i[0],sum/4])
	return l
print(avg(n))