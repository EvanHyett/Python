class bankAccount():
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"{self.balance} {self.int_rate}")
        return self

    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        return self



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bankAccount(int_rate=0.02, balance=0)

    def make_deposit(self):
        self.account.deposit()
        print(self.account.balance)
    
    def make_withdrawal(self):
        self.account.withdraw()
        print(self.account.balance)

    def display_user_balance(self):
        print(self.account.balance)
        return self

    # def transfer_money(self, amount, user):
    #     self.amount -= amount
    #     user.amount += amount
    #     self.display_user_balance()
    #     user.display_user_balance()

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
evan = User("Evan Hyett", "evan@python.com")

evan.account.deposit(2000).withdraw(100).yield_interest()
monty.account.deposit(1000).yield_interest()
print(evan.account.balance)
print(monty.account.balance)

# new_bankAccount1 = bankAccount(0.01, 1000)
# new_bankAccount2 = bankAccount(0.012, 2000)


# bankAccounts = [new_bankAccount1, new_bankAccount2]

# new_bankAccount1.deposit(500).deposit(300).deposit(300).withdraw(100).yield_interest().display_account_info()
# new_bankAccount2.deposit(500).deposit(200).withdraw(50).withdraw(100).withdraw(75).withdraw(36).yield_interest().display_account_info()
