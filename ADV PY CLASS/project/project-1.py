# transaction System:
balance = 0
transactions = []

PASSWORD = "giet@123"
attempts = 3

# Password check:
while attempts > 0:
    user_pass = input("Enter your password: ")

    if user_pass == PASSWORD:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Wrong password attempts left:", attempts)

if attempts == 0:
    print("Too many wrong attempts")
else:

  while True:
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.CheckBalance")
    print("4.Transaction History")
    print("5.Exit")

    choice= int(input("Enter your choice:"))
    if choice == 1:
        amt = int(input("Enter Deposit Amount"))
        balance +=amt
        transactions.append("Deposited" + str(amt))
        print("Amount Deposited")

    elif choice == 2:
        amt = int(input("Enter Withdrawal Amount"))
        if amt <= balance:
            balance -=amt
            transactions.append("Withdrawl: " +str(amt))
            print("Amount Withdrawn")

        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Current Balance: ",balance)

    elif choice == 4:
        print("\nTransaction History")
        if len(transactions) == 0:
            print("No Transaction Yet")
        else:
            for t in transactions:
                print(t)

    elif choice == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
