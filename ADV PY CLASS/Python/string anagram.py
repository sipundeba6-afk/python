n1=input("enter the string: ")
n2=input("enter the string: ")
s1=n1.lower()
s2=n2.lower()
if len(s1)!=len(s2):
    print("NOT ANAGRAM!!")
else:
    sys=True
    for i in s1:
        if s1.count(i)!=s2.count(i):
            print("NOT ANAGRAM!!")
            sys=False
            break
    if sys==True:
        print("ANAGRAM!!")
    else:
        print("NOT ANAGRAM!!")
        
