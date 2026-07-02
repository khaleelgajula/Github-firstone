# Initial balance
balance = 1000

# Function to check balance
def check_balance():
    print(f"Your current balance is: ₹{balance}")

# Function to deposit money
def deposit(amount):
    global balance
    try:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        balance += amount
        print(f"₹{amount} has been deposited successfully.")
        print(f"Updated balance after deposit: ₹{balance}")
    except ValueError as e:
        print("Error:", e)

# Function to withdraw money
def withdraw(amount):
    global balance
    try:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > balance:
            raise Exception("Insufficient balance.")
        balance -= amount
        print(f"₹{amount} has been withdrawn successfully.")
        print(f"Updated balance after withdrawal: ₹{balance}")
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)

# Menu-driven program
while True:
    print("\n----- Bank Menu -----")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        try:
            amt = float(input("Enter amount to deposit: "))
            deposit(amt)
        except ValueError:
            print("Invalid input! Please enter a number.")
    elif choice == '3':
        try:
            amt = float(input("Enter amount to withdraw: "))
            withdraw(amt)
        except ValueError:
            print("Invalid input! Please enter a number.")
    elif choice == '4':
        print("Thank you for using the banking system.")
        break
    else:
        print("Invalid choice! Please try again.")