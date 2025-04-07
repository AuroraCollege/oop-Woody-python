class Bank_Account: 
    def __initi__(self , accountNum , AccountHol , balance , pin):
        self.accountNum = accountNum
        self.AccountHol = AccountHol
        self.__balance = balance
        self.__pin = pin

MR_KELLY = Bank_Account(1, 'M.Kelly', 90000, 666666)

def add_balance(self, amount):
    self.__balance += amount

def withdraw(self,amount,pin):
    if self.pin == pin and self.__balance >= amount:
        self.__balance -= amount