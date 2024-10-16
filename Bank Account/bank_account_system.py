class BankAccount():
    def __init__(self, balance, name, account_number):
        self._balance = balance
        self.account_holder_name = name
        self.account_number = account_number

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('The amount has to be a positive number')
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('The amount has to be a positive number')
        if self._balance < amount:
            raise ValueError('Not enough money in the account')

        self._balance -= amount

    @property
    def balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, balance, name, account_number, interest):
        self.interest = interest
        super().__init__(balance, name, account_number)

    def one_year_interest(self):
        if self._balance < 0:
            raise ValueError('No amount')
        
        self._balance = self._balance * (1+self.interest)

    @property
    def balance(self):
        return self._balance


save_account = SavingsAccount(2000, 'Ryan', '124151', 0.1)
save_account.one_year_interest()
print(save_account.balance)
