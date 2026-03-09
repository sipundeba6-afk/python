#transaction System:
balance = 0
transactions = []

PASSWORD = "giet@123"
temps = 3

# Password check:
def check_paswrd():
    attempts=temps
    while attempts > 0:
        user_pass = input("Enter your password: ")
        if user_pass == PASSWORD:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print("Wrong password attempts left:", attempts)
    print("Too many wrong attempts")
    return False

def deposit():
    global balance
    amt = int(input("Enter Deposit Amount"))
    balance=balance+amt
    transactions.append("Deposited",amt)
    print("Amount Deposited")

def withdraw():
    global balance
    amt = int(input("Enter Withdrawal Amount"))
    if amt <= balance:
        balance=balance-amt
        transactions.append("Withdrawl: " ,amt)
        print("Amount Withdrawn")
    else:
        print("Insufficient Balance")

def check_bal():
    print("current balance is: ",balance)
         
def transaction():
    print("\nTransaction History")
    if len(transactions) == 0:
        print("No Transaction Yet")
    else:
        for t in transactions:
            print(t)

def choice():
    while True:
        print("\n1.Deposit")
        print("2.Withdraw")
        print("3.CheckBalance")
        print("4.Transaction History")
        print("5.Exit")
        choices=int(input("Enter your choice:"))
        if choices==1:
            deposit()
        elif choices==2:
            withdraw()
        elif choices==3:
            check_bal()
        elif choices==4:
            transaction()
        elif choices==5:
            print("Thank You")
            break
        else:
            print("Invalid Choice")

if check_paswrd():
    choice()
