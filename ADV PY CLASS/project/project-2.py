hostel={101:None, 102:None, 103:None, 104:None, 105:None, 106:None}

while True:
    print("\n1.check room availablity")
    print("2.Allot a room")
    print("3.show occupied/empty room")
    print("4.Exit")
    choice= int(input("enter the choice: "))

    if choice==1:
      room_no=int(input("enter the room no: "))

      if hostel[room_no] is None :
        print("room is available")
      else:
        print("room is not available")

    elif  choice==2:
      n=input("enter the student name:")
      student={"name":n}
      if hostel[room_no]is None:
        hostel[room_no]=student
        print("room alloted!!!")
      else:
        print("room is occupied!!!")

    elif  choice==3:
      empty=0
      occupied=0
      for i in hostel:
        if hostel[i] is None:
          empty +=1
        else:
          occupied+=1
      print("total occupied rooms: ",occupied)
      print("total empty rooms: ", empty)


    elif  choice==4:
      print("EXIT!!!!!")

      break

    else:
        print("Invalid choice \nTHANK YOU!!!!!!!!!")
