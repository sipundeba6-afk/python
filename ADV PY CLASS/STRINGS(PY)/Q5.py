str=input("enter the string: ")
lower_case=0
upper_case=0
digit=0
special_char=0
for i in str:
    if i.islower():
        lower_case= lower_case+1
    elif i.isdigit():
        digit=digit+1
    elif not i.isalnum():
        special_char=special_char+1
    else:
        upper_case=upper_case+1
print("no of upper_case: ",upper_case)
print("no of lower_case: ",lower_case)
print("no of digit: ",digit)
print("no of special_char: ",special_char)
