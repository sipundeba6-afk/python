showtimes=["10 AM", "1 PM", "6 PM"]
seats=["A1", "A2", "A3", "A4", "A5"]

def show_showtimes():
    print("Available Showtimes:")
    for s in showtimes:
        print(s)

def show_seats():
    print("Available Seats:")
    for seat in seats:
        print(seat)

def book_ticket():
    name=input("Enter your name: ")
    
    show_showtimes()
    time=input("Select showtime: ")

    show_seats()
    seat=input("Select seat: ")

    if seat in seats:
        seats.remove(seat)
        print("\n----- Booking Confirmation -----")
        print("Name:", name)
        print("Showtime:", time)
        print("Seat:", seat)
        print("Ticket Booked Successfully!")
    else:
        print("Seat not available")

while True:
    print("\n1.Check Showtimes")
    print("2.Book Ticket")
    print("3.Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        show_showtimes()

    elif choice==2:
        book_ticket()

    elif choice==3:
        break
