st=int(input("enter the no of elements you want: "))
lst=[]
for i in range(st):
    s=int(input("enter the elements: "))
    lst.append(s)
search=int(input("enter the element to be searched: "))
if search in lst:
           print("number exist!!!")
else:
    print("number does not exist!!!")
