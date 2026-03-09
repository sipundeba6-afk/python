class Warehouse:

    def __init__(self):
        self.stock=0

    def add(self):
        a=int(input("Enter the goods: "))
        self.stock=self.stock+a
        print("!!Goods added!!")

    def remove(self):
        r=int(input("Enter goods to be removed: "))
        if r<=self.stock:
            self.stock=self.stock-r
            print("x-x-x-x Goods removed x-x-x-x")
        else:
            print("Not enough stock")

    def report(self):
        print("Total goods in the warehouse:",self.stock)

    def forecast(self):
        d=int(input("Enter expected demand: "))
        if d>self.stock:
            print("Need more goods")
        else:
            print("Stock is enough")


obj=Warehouse()

while True:
    print("\n1.Add Goods")
    print("2.Remove Goods")
    print("3.Inventory Report")
    print("4.Forecast Demand")
    print("5.Exit")

    ch=int(input("Enter choice: "))

    if ch==1:
        obj.add()

    elif ch==2:
        obj.remove()

    elif ch==3:
        obj.report()

    elif ch==4:
        obj.forecast()

    elif ch==5:
        break
