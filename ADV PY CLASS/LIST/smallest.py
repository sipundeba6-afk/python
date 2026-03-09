lst=[]
s=int(input("enter the no of items you want: "))
for i in range(s):
    st=int(input("enter the nos: "))
    lst.append(st)
smallest=lst[0]         
for st in lst:          
    if st<smallest:
        smallest=st
print(smallest)
