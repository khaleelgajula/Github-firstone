#main py
import bank
print(f' intial Bank balance:{bank.check_balance}')
print(f'deposit amount is : {bank.deposit(1000)}')
print(f'withdraw amount is :{bank.withdraw(5000)}')
print(f'fanal balance is :{bank.check_balance()}')