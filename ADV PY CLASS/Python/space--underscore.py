n=input("enter the string: ")
s=""
for i in n:
    if i == " ":
        s=s+"_"
    else:
        s=s+i
print("updated string is: ",s)
