lst=[]
num=int(input("enter the no of elements you want: "))
count=0
for i in range(num):
    n=int(input("enter the nos: "))
    lst.append(n)
for x in lst:
    count=count+1
print("no of elemenst in a list are: ",count)
print("the list is : ",lst)
