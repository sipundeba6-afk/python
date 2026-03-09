str=input("enter the string: ")  #BANANA
s=" "
for i in str:                   #i=B A N A N A
    if i not in s:              #s=B
       s=s+i                    #S=BAN
print(s)
