class FreeLancer:
     def rgstr(self):
         self.reg_no=int(input("enter the reg_no: "))
         self.reg_name=input("enter the name: ")
         self.reg_address=input("enter the address: ")
         self.reg_ph=int(input("enter the phone_no: "))
     def project(self):
         self.prjct=input("enter the project name: ")
         print(self.project,"assigned to", self.reg_name)
     def payments(self):
         self.payment=int(input("enter the amount: "))
         print(self.payment,"amount", self.reg_name)
     def show(self):
         print("\nFreelancer Details:")
         print("Reg No:", self.reg_no)
         print("Name:", self.reg_name)
         print("Address:", self.reg_address)
         print("Phone:", self.reg_ph)

obj1=FreeLancer()
while True:
    print("\n1. Register Freelancer")
    print("2. Assign Project")
    print("3. Process Payment")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice==1:
        obj1.rgstr()
        print("successfully registered!!")

    elif choice==2:
        obj1.project()
        print("successfully assigned project!!")


    elif choice==3:
        obj1.payments()

    elif choice==4:
        obj1.show()

    elif choice==5:
        break
