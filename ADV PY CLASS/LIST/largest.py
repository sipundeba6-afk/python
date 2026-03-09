lst=[]
s=int(input("enter the no of items you want: "))
for i in range(s):
    st=int(input("enter the nos: "))
    lst.append(st)
largest=lst[0]         #[10]
for st in lst:          #[10 , 20 , 30]
    if st>largest:
        largest=st
print(largest)
