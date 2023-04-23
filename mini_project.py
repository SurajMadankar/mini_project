class Account:
    balance=0
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
        
    def title(self):
        print(self.title)
    def balance(self):
        return(self.balance)
    def credi(self,amount):
        balance=self.balance+amount
        return balance
    def getbalance(self,amount):
        balance=self.balance+amount
        print(balance)
    def debit(self,amount):
        balance=self.balance-amount
        print(balance)
        if amount<= balance:
            print ("ATM you can use")
        else:
            print("manage your account")
class CheckingAccount(Account):

    def __init__(self,title,balance,interstRate):
        super().__init__(title, balance)
        self.interestRate=interstRate
    def  interestamount(self):
        interestamount=self.interestRate*self.balance
        c=interestamount/100
        print(c)
 
         
class SavingsAccount(Account):

    def __init__(self,title,balance,interstRate):
        super().__init__(title, balance)
        self.interestRate=interstRate
    def  interestamount(self):
        interestamount=self.interestRate*self.balance
        c=interestamount/100
        print(c)
 
class BUsinessAccount(Account):

    def __init__(self,title,balance,interstRate):
        super().__init__(title, balance)
        self.interestRate=interstRate
    def  interestamount(self):
        interestamount=self.interestRate*self.balance
        c=interestamount/100
        print(c)
 

a=Account("mini project",3000)
a.debit(4000)