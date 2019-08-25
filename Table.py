#print table of given number
x=int(input('enter Number :'))
i=1
s=0
while i<=10:
	s=s+x
	print("{} * {} = {}".format(x,i,s))
	i+=1
