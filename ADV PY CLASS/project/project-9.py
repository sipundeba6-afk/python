total_spots = 2

parking={}

def vehicle_entry():
    if len(parking)<total_spots:
        vehicle = input("Enter vehicle number: ")
        hrs=int(input("Enter parking hours: "))
        parking[vehicle]=hrs
        print("Vehicle parked successfully!")
    else:
        print("Parking Full!")

def vehicle_exit():
    vehicle=input("Enter vehicle number to exit: ")
    if vehicle in parking:
        hrs = parking[vehicle]
        fee = hrs*5
        print("Parking Fee =",fee)
        del parking[vehicle]
        print("Vehicle exited.")
    else:
        print("Vehicle not found.")

def ava_spots():
    spots = total_spots - len(parking)
    print("Available spots:", spots)

def show_vehicles():
    print("Parked Vehicles:", parking)

while True:
    print("\n1.Vehicle Entry")
    print("2.Vehicle Exit")
    print("3.Available Spots")
    print("4.Show Vehicles")
    print("5.Exit")

    choice = int(input("Enter choice: "))
    if choice == 1:
        vehicle_entry()
    elif choice == 2:
        vehicle_exit()
    elif choice == 3:
        ava_spots()
    elif choice == 4:
        show_vehicles()
    elif choice == 5:
        break
