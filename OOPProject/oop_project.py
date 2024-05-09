from bank_account import *

Alon = BankAccount(1000, "alon")
Sara = BankAccount(2000, "Sara")
Alon.get_balance()
Sara.get_balance()

Sara.deposit(500)
Alon.get_pin()
Alon.withdraw(10000)
Alon.withdraw(10)
Alon.transfer(10000,Sara)
Alon.transfer(100,Sara)

print(Alon.get_num_accounts())
print(Sara.get_num_accounts())
print(BankAccount.get_num_accounts())

Jim = InterestRewardsAcct(1000,"Jim")
Jim.get_balance()
Jim.deposit(100)
Jim.transfer(100,Alon)

moshe = SavingsAcct(1000,"moshe")
moshe.get_balance()
moshe.withdraw(100)
moshe.deposit(100)
moshe.transfer(10000,Sara)
moshe.transfer(1000,Sara)
