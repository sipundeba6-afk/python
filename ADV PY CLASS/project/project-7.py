PIN=input("enter the password: ")
while True:
    print("\n1.check stage 1")
    print("2.check stage 2")
    print("3.check stage 3")
    print("4.Exit")
    choice= int(input("enter the choice: "))

    if choice==1:
        found=False
        for ch in PIN:
          if ch.isalpha():
              found=True
              break
        if found==True:
            print("STAGE 1 PASS!!!")
        else:
            print("STAGE 1 FAIL!!!")

    elif choice==2:
        found=False
        for num in PIN:
          if num.isdigit():
              found=True
              break
        if found==True:
            print("STAGE 2 PASS!!!")
        else:
            print("STAGE 2 FAIL!!!")

    elif choice==3:
        found=False
        for sp in PIN:
          if not sp.isalnum():
              found=True
              break
        if found==True:
            print("STAGE 3 PASS!!!")
        else:
            print("STAGE 3 FAIL!!!")

    elif choice==4:
        print("!!EXIT!!")
        break
    else:
        print("Invalid choice \nTHANK YOU!!!!!!!!!")

   
   


