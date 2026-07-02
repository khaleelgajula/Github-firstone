#bank

balance= 98000

def deposit(amount):
    global balance
    balance= balance+amount
    return balance
def withdraw (amount):
    global balance
    if amount<=balance:
        balance=balance-amount
        return balance
    else:
        return 'insufficient balance'
def check_balance():
    return balance
