str=input("enter the string: ")
count_str=0
count_num=0
for i in str:
    if i.isalpha():
        count_str=count_str+1
    elif i.isdigit():
        count_num=count_num+1
print("no of letters: ",count_str)
print("no of digits: ",count_num)
