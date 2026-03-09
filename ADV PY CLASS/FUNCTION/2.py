def pal(n): 
    if (n==n[::-1]):
        print("PALINDROME")
    else:
        print("NOT PALINDROME")
text=input("enter the string: ")
pal(text)
