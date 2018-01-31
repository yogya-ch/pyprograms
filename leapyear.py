n=int(input("Give a year ; "))
def f(x):
	if (x%4==0 and x%100!=0):
		if(x%400==0):
			return("Leap year")
		else:
			return("not Leap year")
print(f(n))