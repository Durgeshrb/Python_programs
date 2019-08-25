#print the number is divisible by 7 and mulitple by 5 between given range
i=int(input('enter the first number of given range '))
j=int(input('enter the last number of given range '))
print('the nubers are:')
while i<=j:
	if i%7==0 and i%5==0:	
		print(i)
	i+=1	
	
