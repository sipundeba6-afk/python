class Billing:

    def scan_product(self):
        self.product=input("Enter product name: ")
        self.price=float(input("Enter product price: "))
        print(self.product, "scanned successfully")

    def discount(self):
        self.dis=float(input("Enter discount (%): "))
        self.final_price=self.price-(self.price * self.dis / 100)

    def generate_bill(self):
        print("\n------ BILL ------")
        print("Product:", self.product)
        print("Price:", self.price)
        print("Discount:", self.dis, "%")
        print("Total Amount:", self.final_price)

    def record(self):
        print("Transaction recorded successfully")


obj=Billing()

while True:

    print("\n1. Scan Product")
    print("2. Apply Discount")
    print("3. Generate Bill")
    print("4. Record Transaction")
    print("5. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        obj.scan_product()

    elif choice==2:
        obj.discount()

    elif choice==3:
        obj.generate_bill()

    elif choice==4:
        obj.record()

    elif choice==5:
        break
