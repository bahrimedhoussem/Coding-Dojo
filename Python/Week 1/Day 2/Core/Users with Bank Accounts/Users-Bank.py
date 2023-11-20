class User:
    def __init__(self, name, email, interest_rate=0.2, balance=0):
        self.name = name
        self.email = email 
        self.account = BankAccount(interest_rate, balance)

    def make_deposit(self ,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self ,amount):
        self.account.Withdrawal(amount)
        return self 

    def display_user_balance(self ,amount):
        self.account.display_account_info() 
        return self

houssem = User("houssem", "houssembahri011@gmail.com",interest_rate=0.2,balance=1000)
houssem.make_deposit(1000).make_withdrawal(800).display_user_balance()

        