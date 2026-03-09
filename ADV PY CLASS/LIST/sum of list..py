lst=[]
s=int(input("enter the no of items you want: "))
sum=0
for i in range(s):
    st=int(input("enter the nos: "))
    lst.append(st)
for x in lst:
    sum=sum+x
print("sum of the list: ",sum)
