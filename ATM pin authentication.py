# ------ATM PROJECT--------
pin=7788
balance=1000.0
attempts=0

#PIN authentication using while
while attempts<3:
    entered = int(input("Enter PIN:"))
    if entered==pin:
        break
    else:
        print("Wrong pin")
        attempts+=1
else:
    print("Account locked")
    exit()
#Main  Menu using While
while True:
    print("\n 1.Balance \n 2.Deposit \n3.Withdraw \n4.Exit")
    choice = input('choose:')
    if choice =="1":
        print(f"Balance:{balance}")
    elif choice =="2":
        amt=float(input("Deposit:"))
        balance+=amt
    elif choice =="3":
        amt=float(input("withdraw:"))
        if amt <= balance:
            balance-=amt
        else:
            print("insuficient funds")
    elif choice =="4":
        print("Goodbye")
        break
    else:
        print("Invalid option")