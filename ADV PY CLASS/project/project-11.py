class Password:
    def add(self):
        self.password = input("Enter the password: ")
    def edit(self):
        print("Password before:", self.password)
        self.password = input("Enter new password: ")
    def show(self):
        print("Current password:", self.password)
obj1 = Password()
while True:
    print("\n1. ADD PASSWORD")
    print("2. EDIT PASSWORD")
    print("3. SHOW PASSWORD")
    print("4. EXIT")
    choice = int(input("Enter choice: "))
    if choice == 1:
        obj1.add()
    elif choice == 2:
        obj1.edit()
    elif choice == 3:
        obj1.show()
    elif choice == 4:
        break

