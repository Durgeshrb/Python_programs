#create bank account and perform deposite credit operation and after this closethe account
class bank:
    def __init__(self):
        self.u=0
        self.c=0
        self.d=0
        self.b=0
        self.pw=0
        self.u1=0
        self.pw2=0
        self.y=0
    def createacc(self):
        self.u=input('enter user name')
        self.pw=int(input('enter password name'))
        self.b=int(input('plz deposite some cash tocreate account'))
        print('thank you.your account is created')
    def login(self):
        self.u1=input('enter user name')
        if self.u1==self.u:
            self.pw2=int(input('enter password'))
            if self.pw2==self.pw:
                obj.welcome()
        else:
            print('enter valid usr name')
    def welcome(self):
        self.y=int(input('enter 1 for deposite and 2 for credit and 3 for check balence'))
        if self.y==2:
            self.c=int(input('enter ammount to credit'))
            self.b=self.b-self.c
        if self.y==1:
            self.d=int(input('enter amount to deposite'))
            self.b=self.b+self.d
        if self.y==3:
            print('yur balance is',self.b)
obj=bank()
while True:
    f=int(input('\n1. for create account\n2.log in\n'))
    if f==1:
        obj.createacc()
    if f==2:
        obj.login()

    
    
    
    


