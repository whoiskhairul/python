class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry!not enough balance.")

    def statement(self):
        print("Account balance Euro {}".format(self.balance))

    class Current(Account):
        def __init__(self, name, balance):
            supper.__init__(name, balance, min_balance=-1000)


x = Current("Khairul", 500)
