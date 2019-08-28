while True:	
	d=int(input('press 1 for decimal to binary\npress 2 for binary to decimal:'))
	if d==1:
		n=int(input('enter decimal number'))
		print('binary number is:')
		p=1
		s=0
		while n>0:
			r=n%2
			x=r*p
			s=(s+x)
			p=p*10
			n=n/2
		print(s)
	if d==2:
		n=int(input('enter binary number'))
		print('decimal number is:')
		p=1
		s=0
		while n>0:
			r=n%10
			x=r*p
			s=(s+x)
			p=p*2
			n=n/10
		print(s)
	else:
		print('enter right choice')
