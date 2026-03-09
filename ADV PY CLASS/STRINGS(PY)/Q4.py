#WAP TO INPUT A LINE AND ALL UPRC - LWRC AND VISE-VERSA
str=input("enter the sentence: ")
temp=" "
for i in str:
    if i.islower():
        temp=temp+i.upper()
    else:
        temp=temp+i.lower()
print(temp)
        
