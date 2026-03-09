colour=input("enter the traffic light colour: ")
while True:
    print("\n1.red light")
    print("2.yellow light")
    print("3.green light")
    print("4.Exit")
    choice= int(input("enter the choice: "))

    if choice==1:
        if colour=="red":
            print("STOP THE VEHICLE!!!")
        else:
            print("DON'T STOP!!!")

    elif choice==2:
        if colour=="yellow":
            print("START THE VEHICLE!!!")
        else:
            print("DON'T START!!!")

    elif choice==3:
        if colour=="green":
            print("GO!!!")
        else:
            print("DON'T GO!!!")


    elif choice==4:
        print("!!EXIT!!")
        break
    else:
        print("Invalid choice \nTHANK YOU!!!!!!!!!")

   
   


