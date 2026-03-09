def total_students(*students):                                                  #this is declare a function ,*students = Variable length arguments (*args).
    print("\nTotal Number of Students =", len(students))                        #the space in the second line is basically the indentation.

def student_details(**data):                                                    #this is nested function- function inside function.
    names = []

    print("Student Details :")
    for key, value in data.items():                                             #for loop
        print(key, ":", value)
        names.append(value)
    total_students(*names)
    for i in names:
        bank(i)

def bank(name):                                                                 #(name)-arguments
    print("\nBank Details of", name)
    accno = int(input("Enter Account No : "))
    damt = int(input("Enter Deposit Amount : "))
    wamt = int(input("Enter Withdraw Amount : "))
    total_bal = 0
    total_bal = deposit(damt, total_bal)                                        # function call of deposit
    withdraw(wamt, total_bal)                                                   #function call of withdraw

def deposit(damt, total_bal):
    total_bal = total_bal + damt
    print("amount deposited: ", damt)
    print("total balance: ", total_bal)
    return total_bal                                                            #important return

def withdraw(wamt, total_bal):
    if total_bal >= wamt:                                                       #if statement- use to do the condition, runs until the condition states true.
        total_bal = total_bal - wamt
        print("amount withdrawn: ", wamt)
        print("total balance: ", total_bal)
    else:                                                                       #else- runs when the if statement fails to hold the true condition
        print("Insufficient Balance")

student_details(student1="Tanisha", student4="Krishna")                          #student_detail()- this is called function call
