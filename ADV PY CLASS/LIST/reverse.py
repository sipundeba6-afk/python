lst=[]
rev=0
s=int(input("enter the no of items you want: "))
for i in range(s):
    st=int(input("enter the nos: "))
    lst.append(st)
for x in lst:
    rev=rev%10
