class BankAccount:
    def __init__(self, balance, interest_rate):
        self._balance = balance
        self._interest_rate = interest_rate
        self._transactions = []

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(f'Add {amount} to your account.')
            print(f'Total: {self._balance}')
        else:
            print('Wrong amount!')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
            self._transactions.append(f'Subtract {amount} from your account.')
            print(f'Total: {self._balance}')
        else:
            print('Wrong amount!')

    def add_interest(self):
        interest = self._balance * self._interest_rate / 100
        self._balance += interest
        self._transactions.append(f'Add {interest} to your account.')
        print(f'Total: {self._balance}')

    def history(self):
        for transaction in self._transactions:
            print(transaction)


account = BankAccount(100, 5)
account.deposit(10)
account.withdraw(25)
account.add_interest()
account.history()
