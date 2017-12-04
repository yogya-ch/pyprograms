# Prints the digits in a given number
n=int(input("give a number "))
l=[]
while n>0:
	a=n%10
	l.append(a)
	n=n//10
l.reverse()
for i in l:
	print(i)