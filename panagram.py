n=input("give a sentence ")
s=set()
for i in range(len(n)):
	if i.isalpha():
		set.add(n[i])
if len(s)==26:
	print("It is a panagram")