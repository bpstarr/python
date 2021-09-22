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
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else: 
            print("You are being charged 100$ due to insufficient funds")
            self.balance -= 100
        return self
    def display_account_info(self):
        print(f"{self.balance}")
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
            return self
    @classmethod 
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking": BankAccount(0.05,2000),
            "savings": BankAccount(0.10,4000)
        }
        
    def display_user_balance(self):
        print(f"Users: {self.name}, Checking Balance:{self.account['checking'].display_account_info()}")
        print(f"Users: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self
    def transfer_money(self,amount,user):
        self.amount -= amount
        self.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self
bill = User("Bill")

bill.account['checking'].deposit(200)
bill.display_user_balance()



# checking = BankAccount(0.5,1000)
# savings = BankAccount(1,2000)
# checking.deposit(250).deposit(250).deposit(250).withdraw(500).yield_interest().display_account_info()
# savings.deposit(300).deposit(600).withdraw(100).withdraw(50).withdraw(50).withdraw(20).yield_interest().display_account_info()
# BankAccount.print_all_accounts()

