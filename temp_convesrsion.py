#TEMPERATURE CONVERSION: CELSIUS TO FAHRENHEIT
x=int(input('Enrter 1 for FAHRENHEIT to CELSIUS or 2 for CELSIUS TO FAHRENHEIT coversion '))
if x==1:
	f=int(input('Enter FAHRENHEIT temperature: '))
	a=(f-32)*0.5556
	print('Temperature in Celsius is {}'.format(a))
elif x==2:
	c=int(input('Enter Celsius temperature: '))
	b=(c*1.8)+32
	print('Temperature in fahrenheit is {}'.format(b))
else:
	print('Ennter valid choice')
	
	
