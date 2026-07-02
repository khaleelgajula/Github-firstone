#ATM TRANSACTION

balance=5000
print('------ATM Menu------')
print('1.Check balance')
print('1.Deposit money')
print('3.Withdraw money')

choice=int(input("Enter the 1 or 2 or 3:"))
if choice==1:
    print(f'account balance is:{balance}')
elif choice==2:
    deposit=int(input('Enter the amount to deposit:'))
    balance=balance+deposit
    print(f'{deposit} has been deposited to account:')
    print(f'total balance{balance}')
elif choice==3:
    withdraw_amount=float(input('Enter the amount to withdraw'))
    balance=balance-withdraw_amount
    print(f'{withdraw_amount} has been debited')
    print(f'after withdraw pending bank balance is:{balance}')
