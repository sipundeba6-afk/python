str=input("enter the sentence: ")
vowels="AEIOUaeiou"
count_vowels=0
count_consonent=0
for i in str:
    if i.isalpha():
        if i in vowels:
            count_vowels=count_vowels+1
        else:
            count_consonent=count_consonent+1
print("the no of vowels: ",count_vowels)
print("the no of consonent: ",count_consonent)
