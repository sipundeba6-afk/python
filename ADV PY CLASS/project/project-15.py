class CRM:

    def add_customer(self):
        self.name=input("Enter customer name: ")
        self.phone=input("Enter phone number: ")
        self.id=int(input("Enter id: "))
        print("Customer added successfully!!!!")

    def communication(self):
        self.msg=input("Enter communication note: ")
        print("Communication saved!")

    def show(self):
        print("\nCustomer Name:",self.name)
        print("Phone:",self.phone)
        print("Communication:",self.msg)


obj=CRM()

while True:

    print("\n1.Add Customer")
    print("2.Add Communication Log")
    print("3.Show Customer Info")
    print("5.Exit")

    ch=int(input("Enter choice: "))

    if ch==1:
        obj.add_customer()

    elif ch==2:
        obj.communication()

    elif ch==3:
        obj.show()
        
    elif ch==4:
        break
    
