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



new_bankAccount1 = bankAccount(0.01, 1000)
new_bankAccount2 = bankAccount(0.012, 2000)


bankAccounts = [new_bankAccount1, new_bankAccount2]

new_bankAccount1.deposit(500).deposit(300).deposit(300).withdraw(100).yield_interest().display_account_info()
new_bankAccount2.deposit(500).deposit(200).withdraw(50).withdraw(100).withdraw(75).withdraw(36).yield_interest().display_account_info()
