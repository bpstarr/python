class user:
    def __init__(self,name,email):
        self.name = name
        self.email=email 
        self.account_balance= 0
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
guido = user("Guido Van Rossum","guido@python.com")
monty = user("Monty Python", "monty@python.com")
ball = user("Ball Python","ball@python.com")

guido.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawal(200).display_user_balance()
monty.make_deposit(200).make_deposit(200).make_withdrawal(200).make_withdrawal(200).display_user_balance()
ball.make_deposit(600).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).display_user_balance()
guido.transfer_money(ball, 200).display_user_balance()
guido.display_user_balance()
ball.display_user_balance()