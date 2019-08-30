#take a and b as member variable(operand) and perform operation with function call using class
#addition subtraction multiplication divisio using meber function

class calculator:
	def __init__(self): 
		self.a=0
		self.b=0
		self.c=0
	def sum(self):
		self.c=self.a + self.b
		print('sum result is:',self.c)
	def sub(self):
		self.c=self.a - self.b
		print('sub result is:',self.c)
	def mul(self):
		self.c=self.a * self.b
		print('mul result is:',self.c)
	def div(self):
		self.c=self.a / self.b
		print('div result is:',self.c)


obj=calculator()
obj.a=int(input('enter value of a:'))
obj.b=int(input('enter value of a:'))
x=int(input('press 1 for sum,2for sub 3 for mul 4 for div:'))
if x==1:
	obj.sum()
if x==2:
	obj.sub()
if x==3:
	obj.mul()
if x==4:
	obj.div()
	
