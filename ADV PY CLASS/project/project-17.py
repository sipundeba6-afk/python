def enter_marks():
    name=input("Enter student name: ")
    m1=int(input("Enter marks of subject1: "))
    m2=int(input("Enter marks of subject2: "))
    m3=int(input("Enter marks of subject3: "))

    total=m1+m2+m3
    avg=total/3

    print("\n-----Result-----")
    print("Name:",name)
    print("Total:",total)
    print("Average:",avg)

    if avg>=40:
        print("Result: Pass")
    else:
        print("Result: Fail")

enter_marks()
