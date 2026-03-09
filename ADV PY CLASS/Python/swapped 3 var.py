#swapped using 3 variables
x=int(input("enter 1st no:"))
y=int(input("enter 2nd no:"))
print("the nos before swapped: ",x,y) #x=10,y=20
x=x+y #10+20=30
y=x-y #30-20=10
x=x-y #30-10=20
print("the nos after swapped: ",x,y)
