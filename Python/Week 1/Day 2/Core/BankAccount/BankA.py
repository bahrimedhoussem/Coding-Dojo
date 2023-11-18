class BankAccount: 
     def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance 

     def deposit (self, amount):
        self.balance += amount
        print(f"deposit of {amount} successful . New balance is {self.balance}")
        return self

     def withdraw (self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"withdraw of {amount} successful. new balance is {self.balance}")
        else:     
            print("Insufficient funds. Withdrawal failed")
        return self    

     def display_account_info(self):
        print(f"Account Information - Interest Rate: {self.interest_rate}, Balance: {self.balance}")
        return self

     def yield_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        print(f"Interest of {interest_earned} yielded . New balance {self.balance}" )
        return self

account1 = BankAccount(0.02,balance=1000)
account2 = BankAccount(0.02,balance=2000)   
account1.deposit(500).deposit(200).deposit(100).withdraw(160).yield_interest().display_account_info()  
account2.deposit(500).deposit(100).withdraw(250).withdraw(60).withdraw(20).withdraw(30).display_account_info()





           
