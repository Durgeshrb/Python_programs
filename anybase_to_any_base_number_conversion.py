while True:
	j=int(input('frm which number system:'))
	i=int(input('to which number system:'))
	n=int(input('enter  number:'))
	n1=n
	p=1
	s=0
	while n>0:
		r=n%i
		x=int(r*p)
		s=(s+x)
		p=p*j
		n=n/i	
	'''below statements are for checking user has enter number in right number system or not
		and also check the convertednumber is right or not and print the converted number 
		if it is right'''
	s2=s
	p=1
	s1=0	
	while s>0:
		r=s%j
		x=int(r*p)
		s1=s1+x
		p=p*i
		s=s/j
	if s1==n1:
		print(s2)
	else:
		print('enter a valid number plz')
		
