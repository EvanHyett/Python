class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account_balance = 0

    def makeDeposit(self, amount):
        self.account_balance += amount

    def makeWithdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.first_name)
        print(self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

evan = User("Evan", "Hyett", "evan1hyett@gmail.com")
lindsey = User("Lindsey", "Griffin", "lindseygriff@gmail.com")

evan.makeDeposit(10000)
evan.transfer_money(lindsey, 2000)

evan.display_user_balance()
lindsey.display_user_balance()