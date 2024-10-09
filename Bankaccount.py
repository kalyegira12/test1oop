class Bankaccount:
    # the class variable
    interestrate = 0.05

    #initializing account holder and balance
    def __init__(self, accountholder):
        self.accountholder = accountholder
        self.balance = 0

     # deposit money method
    def deposit(self, amount):
        self.balance += amount 

    # withdraw method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"sorry you have insufficient funds{self.accountholder}") 

    # applying interest method
    def applyinterest(self):
        self.balance += self.balance * Bankaccount.interestrate

    # displaying account information method
    def displayaccountinfo(self):
        print(f"Account holder name: {self.accountholder}, Balance: {self.balance: .2f}") 



#getting instances of account holders
account1 = Bankaccount("Kalyegira")
account2 = Bankaccount("kato")  

 #addding deposits and withdrawals on both accaounts
account1.deposit(20000)
account1.withdraw(1000)
account1.applyinterest()

account2.deposit(30000)
account2.withdraw(3000)
account2.applyinterest()

# displaying the account info of Kalyegira and kato
account1.displayaccountinfo()
account2.displayaccountinfo()             