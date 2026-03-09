str=input("enter the string : ")
vowels="aeiouAEIOU"
result=" "
for i in str:
    if i not in vowels:
        result=result+i
print("the non vowel sentence is: ",result) 
        
