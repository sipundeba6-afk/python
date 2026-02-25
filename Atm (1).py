accounts = {}

def create_account():
    acc_no = input("Enter New Account Number👉🏻: ")

    if acc_no in accounts:
        print("Account already exists😎!")
        return

    name = input("Enter Account Holder Name👉🏻: ")
    acc_type = input("Enter Account Type (Saving/Zero)👉🏻: ")
    phone = input("Enter Phone Number👉🏻: ")
    balance = float(input("Enter Initial Deposit Amount👉🏻: "))

    pin = input("Generate 4-digit ATM PIN👉🏻: ")

    accounts[acc_no] = {
        "name": name,
        "type": acc_type,
        "phone": phone,
        "balance": balance,
        "pin": pin,
        "history": ["Account created with balance😎" + str(balance)]
    }

    print("Account Created Successfully🙂‍!")

def login():
    acc_no = input("Enter Account Number👉🏻: ")
    pin = input("Enter ATM PIN👉🏻: ")

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print("Login Successful🙂‍!")
        atm_menu(acc_no)
    else:
        print("Invalid Account Number or PIN😖")

def atm_menu(acc_no):
    while True:
        print("\n---🏧ATM MENU🏧---")
        print("1. 💵Balance Check")
        print("2. 💳Debit")
        print("3. 💳Credit")
        print("4. 📲Change Phone Number")
        print("5. 🔐Change ATM PIN")
        print("6. 💵Transaction History")
        print("7. 🚪Exit")

        choice = input("Choose Option👉🏻: ")

        if choice == "1":
            balance_check(acc_no)
        elif choice == "2":
            debit(acc_no)
        elif choice == "3":
            credit(acc_no)
        elif choice == "4":
            change_phone(acc_no)
        elif choice == "5":
            change_pin(acc_no)
        elif choice == "6":
            transaction_history(acc_no)
        elif choice == "7":
            break
        else:
            print("Invalid Option😖")

def balance_check(acc_no):
    print("Available Balance👉🏻:", accounts[acc_no]["balance"])


def debit(acc_no):
    amount = float(input("Enter Amount to Debit👉🏻: "))

    if amount <= accounts[acc_no]["balance"]:
        accounts[acc_no]["balance"] -= amount
        accounts[acc_no]["history"].append("Debited: " + str(amount))
        print("Amount Debited Successfully😎")
    else:
        print("Insufficient Balance😖")

def credit(acc_no):
    amount = float(input("Enter Amount to Credit👉🏻: "))

    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["history"].append("Credited: " + str(amount))
    print("Amount Credited Successfully😎")

def change_phone(acc_no):
    new_phone = input("Enter New Phone Number👉🏻: ")
    accounts[acc_no]["phone"] = new_phone
    accounts[acc_no]["history"].append("Phone Number Changed")
    print("Phone Number Updated Successfully😎")

def change_pin(acc_no):
    new_pin = input("Enter New 4-digit PIN👉🏻: ")
    accounts[acc_no]["pin"] = new_pin
    accounts[acc_no]["history"].append("ATM PIN Changed")
    print("ATM PIN Updated Successfully😎")

def transaction_history(acc_no):
    print("\n---💵Transaction History💵---")
    for record in accounts[acc_no]["history"]:
        print(record)

def main():
    while True:
        print("\n==== ATM SYSTEM ====")
        print("1.🙂‍Create Account")
        print("2.🔐Login to ATM")
        print("3. Exit")

        option = input("Choose Option👉🏻: ")

        if option == "1":
            create_account()
        elif option == "2":
            login()
        elif option == "3":
            print("Thank You for visiting | see you again😎!")
            break
        else:
            print("Invalid Choice😖")


main()
