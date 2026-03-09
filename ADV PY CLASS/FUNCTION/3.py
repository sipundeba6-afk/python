def cnt(string):
    vowels="AEIOUaeiou"
    count=0
    for i in string:
        if i in vowels:
            count=count+1
    print(count)
text=input("enter the string: ")
cnt(text)
