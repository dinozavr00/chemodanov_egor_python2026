class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        self._balance -= amount

    def __str__(self):
        return f"Баланс: {self._balance} руб."


bankAccount = BankAccount(0)
bankAccount.deposit(9999)
print(bankAccount)
bankAccount.withdraw(9)
print(bankAccount)