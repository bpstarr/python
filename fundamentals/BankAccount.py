class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
            return self
    @classmethod 
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

checking = BankAccount(0.5,1000)
savings = BankAccount(1,2000)
checking.deposit(250).deposit(250).deposit(250).withdraw(500).yield_interest().display_account_info()
savings.deposit(300).deposit(600).withdraw(100).withdraw(50).withdraw(50).withdraw(20).yield_interest().display_account_info()
BankAccount.print_all_accounts()

