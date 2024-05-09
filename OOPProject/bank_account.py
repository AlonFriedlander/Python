import random


class BalanceException(Exception):
    pass


class BankAccount:
    num_accounts = 0  # Class variable to track the number of accounts

    @staticmethod
    def generate_pin():
        return random.randint(1000, 9999)

    @classmethod
    def get_num_accounts(cls):
        return cls.num_accounts

    def __init__(self, initial_amount, acct_name):
        BankAccount.num_accounts += 1
        self.pin = self.generate_pin()
        self.balance = initial_amount
        self.name = acct_name
        print(f"Account '{self.name}' created.\nBalance = ${self.balance:.2f}")
        print(f"PIN for account: {self.pin}")

    def get_balance(self):
        print(f"Account '{self.name}' balance = ${self.balance:.2f}")

    def get_pin(self):
        print(f"Account '{self.name}' pin = {self.pin}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry,account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nwithdraw complete")
            self.get_balance()
        except BalanceException as error:
            print(f'\nwithdraw interrupts: {error}')

    def transfer(self, amount, account):
        try:
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
        except BalanceException as error:
            print(f'\nTransfer interrupted: {error}')


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\ndeposit complete")
        self.get_balance()


class SavingsAcct(InterestRewardsAcct):
    saving = 5  # Class variable to store the withdrawal fee

    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.saving)
            self.balance = self.balance - (amount - self.saving)
            print("\nwithdraw complete")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted : {error}')
