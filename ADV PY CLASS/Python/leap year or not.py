#Write a Python program to check whether a given year is a leap year or not:
yr=int(input("enter the year: "))
if(yr%400==0 & yr%100!=0):
    print("its a leap year")
elif(yr%4==0):
    print("its a leap year")
else:
    print("its not a leap year")
