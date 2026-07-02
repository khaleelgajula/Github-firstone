# 1.single exception handling

try:
    a=45
    b=0
    result=a/b
    print(result)
except ZeroDivisionError:
    print('can not divide by error')

try:
    list=[10,20,30]
    print(list[4])
except IndexError:
    print('index value out of range')

try:
    num=int('python')
    print(num)
except ValueError:
    print('invalid conversion')

#2.multiple excetion handling
try:
    a=int(input('Enter the value of a:'))
    b=int(input('Enter the value of b:'))
    result=a/b
    print(result)
except ZeroDivisionError:
    print('can not divide by zero')
except ValueError:
    print('invalid user input')
    
try:
    a=45
    b=2
    result=a/b
except ZeroDivisionError:
    print('can not divide by zero')
else:
    print(result)                               #22

try:
    a=45
    b=0
    print(a//b)
except ZeroDivisionError:
    print('error')
finally:
    print('program completed')

# withdraw form a bank a/c
try:
    balance:5000
    withdraw=int(input('Enter amount to withdraw:'))
    if withdraw>balance:
        raise Exception('insuffient balance')
    if balance-withdraw<1000:
        raise Exception('minimum balance 1000 must be maintained in bank amount')
except ValueError as v:
    print('error:' ,v)
except Exception as e:
    print('error:' ,e)
else:
    balance=balance-withdraw
    print(f'{withdraw} has been debited from account')
    print(f'after withdraw updated balance is:{balance}')
finally:
    print('Thank you for using ATM')




#banking operations such as check balance, deposit,withdraw using exception handling
#intial balance 
balance=1000

#function to check balance
def check_balance():
    print(f"your current balance is :₹{balance} ")


#function to deposit money 
def deposit(amount):
    global balance
    try:
        if amount<=0:
            raise ValueError("deposit amount must be greater than zero.")
        balance+=amount
        print(f"{amount} has been deposited successfully.")
        print(f"after deposit updated balance is:{balance}")
    except ValueError as e:
        print("error:" ,e)

#Function to withdraw money
def withdraw (amount):
    global balance
    try:
        if amount<=0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount>balance:
            raise Exception("Insufficient balance.")
        balance-=amount
        print(f"{amount} has been debited")
        print(f"updated balance after withdraw :{balance}")
    except ValueError as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)

#Menu_driven program 
while True:
    print("\n-----BankMenu-----")
    print("1.Check balance")
    print("2.Deposit")
    print("3.withdraw")
    print("4.Exit")

    Choice=input ("Enter your choice:")
    if choice =='1':
        check:balance()
    elif Choice =='2':
        try:
            amt=float(input("Enter amount to deposit:"))
            deposit(amt)
        except ValueError:
            print("Invalid input! please enter a number:")
    elif choice =='3':
        try:
            amt=float (input("Enter amount to withdraw :"))
            withdraw(amt)
        except ValueError:
            print("Invalid input ! please enter a number:")
    elif choice =='4':
        print("Thank you for using the banking system.")
        break
    else:
        print("Invalid choice! please try again.")