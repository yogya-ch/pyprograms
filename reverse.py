#To reverse the number
n=int(input("give a number "))
a=""
while n>0:
	a=a+str(n%10)
	n=n//10
print(a)